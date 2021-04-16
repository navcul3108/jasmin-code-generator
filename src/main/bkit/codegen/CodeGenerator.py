'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Visitor import BaseVisitor
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from AST import *

class MethodEnv():
    """ Init with frame and symbol
    """    
    def __init__(self, frame, sym):     
        self.frame = frame
        self.sym = sym
class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
class CName:
    def __init__(self,n):
        self.value = n
class Index:
    def __init__(self,n):
        self.value = n
class Type(ABC): pass
class IntType(Type): pass
class FloatType(Type):pass
class VoidType(Type):pass
class ClassType(Type):
    def __init__(self,n):
        self.cname = n
class StringType(Type):pass
class BoolType(Type):pass
class MType(Type):
    def __init__(self,i,o):
        self.partype = i #List[Type]
        self.rettype = o #Type	
class ArrayType(Type):
    def __init__(self,et,*s):
        self.eleType = et #Type
        self.dimen = s   #List[int]  

class CodeGenerator():
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("read", MType([], StringType()), CName(self.libName)),
                Symbol("printLn", MType([], VoidType()), CName(self.libName)),
                Symbol("printStrLn", MType([StringType()], VoidType()), CName(self.libName)),
                Symbol("print", MType([StringType()], VoidType()), CName(self.libName)),
    		    Symbol("string_of_int", MType([IntType()], StringType()), CName(self.libName)),
                Symbol("int_of_float", MType([FloatType()], IntType()), CName(self.libName)),
                Symbol("float_to_int", MType([IntType()], FloatType()), CName(self.libName)),
                Symbol("int_of_string", MType([StringType()], IntType()), CName(self.libName)),
                Symbol("float_of_string", MType([StringType()], FloatType()), CName(self.libName)),
                Symbol("string_of_float", MType([FloatType()], StringType()), CName(self.libName)),
                Symbol("bool_of_string", MType([StringType()], BoolType()), CName(self.libName)),
                Symbol("string_of_bool", MType([BoolType()], StringType()), CName(self.libName))
                    ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)


class CodeGenVisitor(BaseVisitor):
    @staticmethod
    def convertLiteralToJvmType(literal):
        litType = type(literal)
        if litType is IntLiteral:
            return IntType()
        elif litType is FloatLiteral:
            return FloatType()
        elif litType is StringLiteral:
            return StringType()
        elif litType is BooleanLiteral:
            return BoolType()
        elif litType is ArrayLiteral:
            dimen = [len(literal.value)]
            eleLiteral = literal.value[0]
            while type(eleLiteral) is ArrayLiteral:
                dimen.append(len(eleLiteral.value))
                eleLiteral = eleLiteral.value[0]
            return ArrayType(CodeGenVisitor.convertLiteralToJvmType(eleLiteral), *dimen)
        else:
            return None

    @staticmethod
    def findWithName(symbols, findingName, funcOnly=False):
        """ Find Symbol with findingName, if funcOnly = True, then this function
        only find in last element

        Args:
            symbols ([type]): [description]
            findingName ([type]): [description]
            funcOnly (bool, optional): [description]. Defaults to False.

        Returns:
            Symbol: [description]
        """        
        if funcOnly:
            res = list(filter(lambda symbol: symbol.name==findingName ,symbols[-1]))
            return res[0] if len(res)>0 else None
        else:
            for subLevel in symbols:
                res = list(filter(lambda symbol: symbol.name==findingName , subLevel))
                if len(res)>0:
                    return res[0]
            return None

    @staticmethod
    def getValuesOfArray(arr: ArrayLiteral):
        """ Get 1d-list values of array, no matter what this array is single or
        multi-dimensions

        Args:
            arr (ArrayLiteral): [description]

        Returns:
            [type]: [description]
        """        
        if type(arr.value[0]) is ArrayLiteral:
            result = []
            for arrLit in arr.value:
                result.extend(CodeGenVisitor.getValuesOfArray(arrLit))
        else:
            result = [lit.value for lit in arr.value]
        return result

    @staticmethod
    def update(symbols, name, newSymbol):
        for subLevel in symbols:
            for idx, sym in enumerate(subLevel):
                if sym.name == name:
                    subLevel[idx] = newSymbol
                    return

    @staticmethod
    def isUnknown(typ: Type):
        if typ == None or (isinstance(typ, ArrayType) and typ.eleType == None):
            return True
        return False

    @staticmethod
    def getTypeOfOperand(op: str):
        if op in ['+', '-', '*', '\\', '%', '<', '>', '<=', '>=', '==', '!=']:
            return IntType()
        elif op in ['+.', '-.', '*.', '\\.', '<.', '>.', '<=.', '>=.', '=/=']:
            return FloatType()
        elif op in ['&&', '||', '!']:
            return BoolType()
        return None

    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MCClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        self.initialGlobs = list()
        for decl in ast.decl:
            self.visit(decl, None)

        # My code start at here
        # e = MethodEnv(None, self.env)
        # self.genMain(e)
        # generate default constructor
        self.genInit()
        # generate class init if necessary
        self.emit.emitEPILOG()
        return c

    def genInit(self):
        methodname,methodtype = "<init>",MType([],VoidType())
        frame = Frame(methodname, methodtype.rettype)
        self.emit.printout(self.emit.emitMETHOD(methodname,methodtype,False,frame))
        frame.enterScope(True)
        varname,vartype,varindex = "this",ClassType(self.className),frame.getNewIndex()
        startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()
        self.emit.printout(self.emit.emitVAR(varindex, varname, vartype, startLabel, endLabel,frame ))
        self.emit.printout(self.emit.emitLABEL(startLabel,frame))
        self.emit.printout(self.emit.emitREADVAR(varname, vartype, varindex, frame))
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        self.emit.printout(self.emit.emitRETURN(methodtype.rettype, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))

    # The following code is just for initial, students should remove it and write your visitor from here
    def genMain(self,o):
        methodname,methodtype = "main",MType([ArrayType(StringType())],VoidType())
        frame = Frame(methodname, methodtype.rettype)
        self.emit.printout(self.emit.emitMETHOD(methodname,methodtype,True,frame))
        frame.enterScope(True)
        varname,vartype,varindex = "args",methodtype.partype[0],frame.getNewIndex()
        startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()
        self.emit.printout(self.emit.emitVAR(varindex, varname, vartype, startLabel, endLabel,frame ))
        self.emit.printout(self.emit.emitLABEL(startLabel,frame))
        self.emit.printout(self.emit.emitPUSHICONST(120, frame))
        sym = next(filter(lambda x: x.name == "string_of_int",o.sym))
        self.emit.printout(self.emit.emitINVOKESTATIC(sym.value.value+"/string_of_int",sym.mtype,frame))
        sym = next(filter(lambda x: x.name == "print",o.sym))
        self.emit.printout(self.emit.emitINVOKESTATIC(sym.value.value+"/print",sym.mtype,frame))
        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        self.emit.printout(self.emit.emitRETURN(methodtype.rettype, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))

    def visitVarDecl(self, ast, c):
        """ Gen global variable or local variable, do not handle with parameter

        Args:
            ast ([type]): [description]
            c (MethodEnv): contain frame and visied symbols
        """        
        varName = ast.variable.name
        inType = CodeGenVisitor.convertLiteralToJvmType(ast.varInit)

        if type(c) is MethodEnv:#local variable
            startLabel, endLabel = c.frame.getStartLabel(), c.frame.getEndLabel()
            index = c.frame.getNewIndex()
            initValueCode, typ = self.visit(ast.varInit, c)

            self.initialVarCode += initValueCode
            self.initialVarCode += self.emit.emitWRITEVAR(ast.variable.name, typ, index, c.frame)

            c.sym[0].append(Symbol(ast.variable.name, typ, Index(index)))

            return self.emit.emitVAR(index, varName, inType, startLabel, endLabel, c.frame), Symbol(varName, inType, Index(index))
        else:#global variable
            self.emit.printout(self.emit.emitATTRIBUTE(varName, inType, False, value=None))

            if isinstance(ast.varInit, ArrayLiteral):
                value = CodeGenVisitor.getValuesOfArray(ast.varInit)
                self.initialGlobs.append((varName, inType, value))
            else:
                self.initialGlobs.append((varName, inType, ast.varInit.value)) 
            self.env.append(Symbol(varName, inType, CName(self.className)))
            return None

    def visitFuncDecl(self, ast, c):
        # We don't know return type of this function, so we save all statement in buffer
        # if we meet return type then save type of this into self.currFuncReturnType
        # otherwise, return type of this function is VoidType
        #print("Function: ", ast.name.name)

        self.expectType = None
        self.isUnreachable = False
        self.isRead = False
        func_sym = CodeGenVisitor.findWithName([self.env], ast.name.name, funcOnly=True)
        self.initialVarCode = ""
        if func_sym!= None:# being called before declaration
            methodEnv = MethodEnv(Frame(func_sym.name, func_sym.mtype.rettype), [[], self.env])
            self.emit.printout(self.emit.emitMETHOD(func_sym.name, func_sym.mtype, True, methodEnv.frame))
            methodEnv.frame.enterScope(True)

            startLabel, endLabel = methodEnv.frame.getStartLabel(), methodEnv.frame.getEndLabel()
            for idx in range(len(ast.param)):
                self.emit.printout(self.emit.emitVAR(idx, ast.param[idx].variable.name, func_sym.mtype.partype[idx], startLabel, endLabel, methodEnv.frame))
                methodEnv.sym[0].append(Symbol(ast.param[idx].variable.name, func_sym.mtype.partype[idx], Index(idx)))
            self.emit.printout(self.emit.emitLABEL(startLabel, methodEnv.frame))

            for decl in ast.body[0]:
                code, sym = self.visit(decl, methodEnv)
                self.emit.printout(code)
                methodEnv.sym[0].append(sym)

            for stmt in ast.body[1]:
                code = self.visit(stmt, methodEnv)
                self.emit.printout(code)

                # print("Code:", code)                
                # print("Stack size:", methodEnv.frame.getStackSize())
                # print('-'*50)

            self.emit.printout(self.initialVarCode)
            self.emit.printout(self.emit.emitLABEL(endLabel, methodEnv.frame))
            self.emit.printout(self.emit.emitRETURN(func_sym.mtype.rettype, methodEnv.frame))
            self.emit.printout(self.emit.emitENDMETHOD(methodEnv.frame))
            methodEnv.frame.exitScope()
        else:
            self.retType = None
            self.paramTypes = [None] * len(ast.param)
            self.paramNames = []

            methodEnv = MethodEnv(Frame(ast.name, None), [[], self.env])
            # Save symbol of parameters temporarily
            for idx, par in enumerate(ast.param):
                self.paramNames.append(par.variable.name)
                if par.varDimen!=[]:
                    methodEnv.sym[0].append(Symbol(par.variable.name, ArrayType(None, *par.varDimen), Index(idx)))
                else:
                    methodEnv.sym[0].append(Symbol(par.variable.name, None, Index(idx)))

            methodEnv.frame.enterScope(True)
            startLabel, endLabel = methodEnv.frame.getStartLabel(), methodEnv.frame.getEndLabel()
            isMain = ast.name.name == "main"

            bodyBuff = ""
            if isMain:
                index = methodEnv.frame.getNewIndex()
                bodyBuff += self.emit.emitVAR(index, 'args', ArrayType(StringType()), startLabel, endLabel, methodEnv.frame)
            else:
                _ = [methodEnv.frame.getNewIndex() for _ in self.paramNames]

            bodyBuff += self.emit.emitLABEL(startLabel, methodEnv.frame)

            for decl in ast.body[0]:
                code, sym = self.visit(decl, methodEnv)
                bodyBuff += code
                methodEnv.sym[0].append(sym)

            if isMain:
                for tup in self.initialGlobs:
                    # tup: (name, type, value)
                    if isinstance(tup[1], ArrayType):
                        bodyBuff += self.emit.emitARRAY(tup[1], tup[2], tup[1].dimen, methodEnv.frame)
                    else:
                        bodyBuff += self.emit.emitPUSHCONST(tup[2], tup[1], methodEnv.frame)
                    bodyBuff += self.emit.emitPUTSTATIC(self.className+'.'+tup[0], tup[1], methodEnv.frame)

            bodyBuff += self.initialVarCode
            self.initialVarCode = ""
            for stmt in ast.body[1]:
                self.isUnreachable = False
                code = self.visit(stmt, methodEnv)
                bodyBuff += code

                # print("Code:", code)                
                # print("Stack size:", methodEnv.frame.getStackSize())
                # print('-'*50)
            bodyBuff += self.emit.emitLABEL(endLabel, methodEnv.frame)

            if self.retType == None:
                self.retType = VoidType()
                bodyBuff += self.emit.emitRETURN(VoidType(), methodEnv.frame)
            if isMain:
                self.paramTypes = [ArrayType(StringType())]
            else:
                for idx in range(len(self.paramNames)):                    
                    if self.paramTypes[idx]==None:
                        self.paramTypes[idx] = IntType()
                    paramCode = self.emit.emitVAR(idx, self.paramNames[idx], self.paramTypes[idx], startLabel, endLabel, methodEnv.frame)
                    bodyBuff = paramCode + bodyBuff
            self.emit.printout(self.emit.emitMETHOD(ast.name.name, MType(self.paramTypes, self.retType), True, methodEnv.frame))
            self.emit.printout(bodyBuff)
            self.emit.printout(self.emit.emitENDMETHOD(methodEnv.frame))
            methodEnv.frame.exitScope()
            self.env.append(Symbol(ast.name.name, MType(self.paramTypes, self.retType), CName(self.className)))

    def visitArrayCell(self, ast, methodEnv):
        isRead = self.isRead
        self.isRead = True
        result = self.visit(ast.arr, methodEnv)[0]
        
        if type(ast.arr) is Id:
            name = ast.arr.name
            sym = CodeGenVisitor.findWithName(methodEnv.sym, name)
            typ = sym.mtype.eleType
        else:#functionCall
            # The function that return array must be defined before calling
            name = ast.arr.method.name
            func_sym = CodeGenVisitor.findWithName(methodEnv.sym, name, funcOnly=True)
            typ = func_sym.mtype.rettype.eleType

        
        if len(ast.idx)==1:
            self.expectType = IntType()
            result += self.visit(ast.idx[0], methodEnv)[0]
        else:
            for idxExpr in ast.idx[:-1]:
                self.expectType = IntType()
                idxCode, _ = self.visit(idxExpr, methodEnv)
                result += idxCode
                result += self.emit.emitAALOAD(methodEnv.frame)
            result += self.visit(ast.idx[-1], methodEnv)[0]
    
        self.isRead = isRead

        if self.isRead:
            result += self.emit.emitALOAD(typ, methodEnv.frame)
        return result, typ

    def visitBinaryOp(self, ast, methodEnv):
        self.isRead = True
        self.expectType = CodeGenVisitor.getTypeOfOperand(ast.op)
        leftCode, _ = self.visit(ast.left, methodEnv)
        self.expectType = CodeGenVisitor.getTypeOfOperand(ast.op)
        rightCode, _ = self.visit(ast.right, methodEnv)

        if ast.op in ['+', '-']:
            opCode = self.emit.emitADDOP(ast.op, IntType(), methodEnv.frame)
            typ = IntType()
        elif ast.op in ['+.', '-.']:
            opCode = self.emit.emitADDOP(ast.op[0], FloatType(), methodEnv.frame)
            typ = FloatType()
        elif ast.op in ['*', '\\']:
            opCode = self.emit.emitMULOP(ast.op, IntType(), methodEnv.frame)
            typ = IntType()
        elif ast.op in ['*.', '\\.']:
            opCode = self.emit.emitMULOP(ast.op[0], FloatType(), methodEnv.frame)
            typ = FloatType()
        elif ast.op == '%':
            opCode = self.emit.emitMOD(methodEnv.frame)
            typ = IntType()
        elif ast.op == '&&':
            opCode = self.emit.emitANDOP(methodEnv.frame)
            typ = BoolType()
        elif ast.op == '||':
            opCode = self.emit.emitOROP(methodEnv.frame)
            typ = BoolType()
        elif ast.op in ['<', '>', '<=', '>=', '==', '!=']:
            opCode = self.emit.emitREOP(ast.op, IntType(), methodEnv.frame)
            typ = BoolType()
        elif ast.op in ['<.', '>.', '<=.', '>=.', '=/=']:
            opCode = self.emit.emitFREOP(ast.op, FloatType(), methodEnv.frame)
            typ = BoolType()
                   
        return leftCode + rightCode + opCode, typ
    
    def visitUnaryOp(self, ast, methodEnv):
        result = list()
        self.expectType = CodeGenVisitor.getTypeOfOperand(ast.op)
        if ast.op == '-':
            self.isRead = True
            result.append(self.emit.emitPUSHICONST(0, methodEnv.frame))
            
            bodyCode, _ = self.visit(ast.body, methodEnv)
            result.append(bodyCode)
            
            result.append(self.emit.emitADDOP('-', IntType(), methodEnv.frame))
            typ = IntType()
        elif ast.op == '!':
            bodyCode, _ = self.visit(ast.body, methodEnv)
            result.append(bodyCode)

            result.append(self.emit.emitNOT(BoolType(), methodEnv.frame))
            typ = BoolType()
        return ''.join(result), typ

    def visitCallExpr(self, ast, methodEnv):
        result = list()
        self.isRead = True

        func_sym = CodeGenVisitor.findWithName(methodEnv.sym, ast.method.name, funcOnly=True)
        isRead = self.isRead            
        self.isRead = True        
        if func_sym == None: # has not been defined
            # Do not set Index for function symbol, let make it when we meet this function declaration
            paramTypes = list()
            for param in ast.param:
                parCode, parType = self.visit(param, methodEnv)
                paramTypes.append(parType)
                result.append(parCode)
            retType = self.expectType
            #Update index later
            func_sym = Symbol(ast.method.name, MType(paramTypes, retType), CName(self.className))
            methodEnv.sym[-1].append(func_sym)
        else: # has been defined
            isRead = self.isRead                        
            for idx, param in enumerate(ast.param):
                self.expectType = func_sym.mtype.partype[idx]
                parCode, _ = self.visit(param, methodEnv)
                result.append(parCode)
        self.isRead = isRead    

        result.append(self.emit.emitINVOKESTATIC(func_sym.value.value+'/'+ast.method.name, func_sym.mtype, methodEnv.frame))
        return ''.join(result), func_sym.mtype.rettype

    def visitIntLiteral(self, ast, methodEnv):
        return self.emit.emitPUSHICONST(ast.value, methodEnv.frame), IntType()

    def visitFloatLiteral(self, ast, methodEnv):
        return self.emit.emitPUSHFCONST(ast.value, methodEnv.frame), FloatType()

    def visitStringLiteral(self, ast, methodEnv):
        return self.emit.emitLDC(ast.value, methodEnv.frame), StringType()

    def visitBooleanLiteral(self, ast, methodEnv):
        return self.emit.emitPUSHICONST("true" if ast.value else "false", methodEnv.frame), BoolType()

    def visitArrayLiteral(self, ast, methodEnv):
        arrayType = CodeGenVisitor.convertLiteralToJvmType(ast)
        values = CodeGenVisitor.getValuesOfArray(ast)
        return self.emit.emitARRAY(arrayType, values, arrayType.dimen, methodEnv.frame), arrayType

    def visitId(self, ast, methodEnv):
        """ Visit an identifier
        Args:
            ast ([type]): [description]
            methodEnv ([type]): [description]
        """        
        sym = CodeGenVisitor.findWithName(methodEnv.sym, ast.name)
        if type(sym.value) is Index:#local variable    
            index = sym.value.value
            if sym.mtype == None:
                sym.mtype = self.expectType
                self.paramTypes[index] = sym.mtype
                CodeGenVisitor.update(methodEnv.sym, ast.name, sym)        
            elif type(sym.mtype) is ArrayType and sym.mtype.eleType== None:
                if isinstance(self.expectType, ArrayType):
                    sym.mtype = self.expectType
                else:
                    sym.mtype.eleType = self.expectType

                CodeGenVisitor.update(methodEnv.sym, ast.name, sym)
                self.paramTypes[index] = sym.mtype

            if sym.mtype == None:
                return "", None
            else:
                if self.isRead:
                    return self.emit.emitREADVAR(ast.name, sym.mtype, index, methodEnv.frame), sym.mtype
                else:
                    return "", sym.mtype
        else:#global variable
            if self.isRead:
                return self.emit.emitGETSTATIC(sym.value.value+'.'+sym.name, sym.mtype, methodEnv.frame), sym.mtype
            else:
                return "", sym.mtype

    def visitAssign(self, ast, methodEnv):
        # rhsType is alway not None
        self.isRead = True
        rhsCode, rhsType = self.visit(ast.rhs, methodEnv)            

        if rhsType == None:#rhs is parameter
            self.isRead = False
            lhsCode, lhsType = self.visit(ast.lhs, methodEnv)
            parName = ast.rhs.name
            sym = CodeGenVisitor.findWithName(methodEnv.sym, parName)

            sym.mtype = lhsType
            CodeGenVisitor.update(methodEnv.sym, parName, sym)

            self.isRead = True
            rhsCode, rhsType = self.visit(ast.rhs, methodEnv)
            self.paramTypes[sym.value.value] = sym.mtype
        elif isinstance(rhsType, ArrayType) and rhsType.eleType==None:#rhs is parameter
            self.isRead = False
            lhsCode, lhsType = self.visit(ast.lhs, methodEnv)

            parName = ast.rhs.arr.name
            sym = CodeGenVisitor.findWithName(methodEnv.sym, parName)

            sym.mtype.eleType = lhsType.eleType
            CodeGenVisitor.update(methodEnv.sym, parName, sym)

            self.isRead = True
            rhsCode, rhsType = self.visit(ast.rhs, methodEnv)
            self.paramTypes[sym.value.value] = sym.mtype
        else:
            self.expectType = rhsType
            self.isRead = False
            lhsCode, _ = self.visit(ast.lhs, methodEnv)

        result = lhsCode
        if type(ast.lhs) is Id:
            name = ast.lhs.name
        else:#Array Cell
            name = ast.lhs.arr.name
 
        result += rhsCode

        lhsSym = CodeGenVisitor.findWithName(methodEnv.sym, name)
        if CodeGenVisitor.isUnknown(lhsSym.mtype):
            lhsSym.mtype = rhsType
            CodeGenVisitor.update(methodEnv.sym, name, lhsSym)

        if type(lhsSym.value) is Index or (type(lhsSym.value) is CName and type(ast.lhs) is ArrayCell):#lhs is local variable
            index = lhsSym.value.value
            if type(ast.lhs) is Id:
                return result + self.emit.emitWRITEVAR(name, rhsType, index, methodEnv.frame)
            else:
                return result + self.emit.emitWRITEVAR2(name, rhsType, methodEnv.frame)
        else:#lhs is global variable
            return result + self.emit.emitPUTSTATIC(self.className+'.'+name, rhsType, methodEnv.frame)

    def visitCallStmt(self, ast, methodEnv):
        funcSym = CodeGenVisitor.findWithName(methodEnv.sym, ast.method.name, funcOnly=True)
        result = []
        isRead = self.isRead
        self.isRead = True
        if funcSym == None:#being called before defined
            funcSym = Symbol(ast.method.name, MType([None]*len(ast.param),VoidType()), CName(self.className))
            for idx, parAST in enumerate(ast.param):
                parCode, parType = self.visit(parAST, methodEnv)
                result.append(parCode)
                funcSym.mtype.partype[idx] = parType
            methodEnv.sym[-1].append(funcSym)
        else:
            for idx, parAST in enumerate(ast.param):
                self.expectType = funcSym.mtype.partype[idx]
                parCode, _ = self.visit(parAST, methodEnv)
                result.append(parCode)

        self.isRead = isRead
                
        result.append(self.emit.emitINVOKESTATIC(funcSym.value.value+'/'+ast.method.name, funcSym.mtype, methodEnv.frame))
        
        return ''.join(result)

    def visitIf(self, ast, methodEnv):
        self.isRead = True
        methodEnv.frame.enterScope(False)
        methodEnv.sym.insert(0, [])

        inLabel, outLabel = methodEnv.frame.getStartLabel(), methodEnv.frame.getEndLabel()
        result = [self.emit.emitLABEL(inLabel, methodEnv.frame)]
        falseLabel = None

        for tup in ast.ifthenStmt[:-1]:
            # tup: (Expr, List[VarDecl], List[Stmt]) 
            falseLabel = methodEnv.frame.getNewLabel()
            self.expectType = BoolType()
            result.append(self.visit(tup[0], methodEnv)[0])

            result.append(self.emit.emitIFFALSE(falseLabel, methodEnv.frame))
            
            for decl in tup[1]:
                code, _ = self.visit(decl, methodEnv)
                result.append(code)
            result.append(self.initialVarCode)
            self.initialVarCode = ""
            for stmt in tup[2]:
                result.append(self.visit(stmt, methodEnv))
            # Neu statement cuoi cung la return, break hoac continue, khong can goto
            if not self.isUnreachable:
                self.isUnreachable = False
                result.append(self.emit.emitGOTO(outLabel, methodEnv.frame))

            result.append(self.emit.emitLABEL(falseLabel, methodEnv.frame))

        # last if statment
        lastIf = ast.ifthenStmt[-1]
        if ast.elseStmt != ([],[]):
            falseLabel = methodEnv.frame.getNewLabel()
        else:
            falseLabel = None

        self.expectType = BoolType()            
        result.append(self.visit(lastIf[0], methodEnv)[0])
        if falseLabel != None:
            result.append(self.emit.emitIFFALSE(falseLabel, methodEnv.frame))
        else:
            result.append(self.emit.emitIFFALSE(outLabel, methodEnv.frame))
        
        for decl in lastIf[1]:
            code, _ = self.visit(decl, methodEnv)
            result.append(code)

        result.append(self.initialVarCode)
        self.initialVarCode = ""
        for stmt in lastIf[2]:
            result.append(self.visit(stmt, methodEnv))

        # Neu statement cuoi cung la return, break hoac continue, khong can goto
        if not self.isUnreachable:
            self.isUnreachable = False
            result.append(self.emit.emitGOTO(outLabel, methodEnv.frame))

        # Else stmt
        if falseLabel!=None:
            result.append(self.emit.emitLABEL(falseLabel, methodEnv))
            for decl in ast.elseStmt[0]:
                code, _ = self.visit(decl, methodEnv)
                result.append(code)
            result.append(self.initialVarCode)
            self.initialVarCode = ""
            for stmt in ast.elseStmt[1]:
                result.append(self.visit(stmt, methodEnv))
        
        result.append(self.emit.emitLABEL(outLabel, methodEnv.frame))
        methodEnv.frame.exitScope()
        methodEnv.sym = methodEnv.sym[1:]
        return ''.join(result)

    def visitFor(self, ast, methodEnv):
        methodEnv.sym.insert(0, [])

        self.isRead = False
        result = []
        self.expectType = IntType()

        result.append(self.visit(ast.idx1, methodEnv)[0])
        result.append(self.visit(ast.expr1, methodEnv)[0])
        idSym = CodeGenVisitor.findWithName(methodEnv.sym, ast.idx1.name)

        isLocal = type(idSym.value) is Index
        index = None
        lexeme = None
        if isLocal:
            index = idSym.value.value
            result.append(self.emit.emitWRITEVAR(idSym.name, IntType(), index, methodEnv.frame))
        else:
            lexeme = idSym.value.value+'.'+idSym.name
            result.append(self.emit.emitPUTSTATIC(lexeme, IntType(), methodEnv.frame))

        startLabel = methodEnv.frame.getNewLabel()
        methodEnv.frame.enterLoop()
        continueLabel, breakLabel = methodEnv.frame.getContinueLabel(), methodEnv.frame.getBreakLabel()
        result.append(self.emit.emitLABEL(startLabel, methodEnv.frame))
        
        isRead = self.isRead
        self.isRead = True
        self.expectType = BoolType()
        conditionalCode, _ = self.visit(ast.expr2, methodEnv) 
        self.isRead = isRead
        
        result.append(conditionalCode)
        
        result.append(self.emit.emitIFFALSE(breakLabel, methodEnv.frame))
        methodEnv.frame.enterScope(False)
        tempStartLabel, tempEndLabel = methodEnv.frame.getStartLabel(), methodEnv.frame.getEndLabel()
        result.append(self.emit.emitLABEL(tempStartLabel, methodEnv.frame))

        for decl in ast.loop[0]:
            code, _ = self.visit(decl, methodEnv)
            result.append(code)

        for stmt in ast.loop[1]:
            self.isUnreachable = False
            result.append(self.visit(stmt, methodEnv))
        result.append(self.emit.emitLABEL(tempEndLabel, methodEnv.frame))
        methodEnv.frame.exitScope()

        result.append(self.emit.emitLABEL(continueLabel, methodEnv.frame))
        if isLocal:
            result.append(self.emit.emitREADVAR(idSym.name, IntType(), index, methodEnv.frame))
        else:
            result.append(self.emit.emitGETSTATIC(lexeme, IntType(), methodEnv.frame))
        
        self.expectType = IntType()
        result.append(self.visit(ast.expr3, methodEnv)[0])
        result.append(self.emit.emitADDOP('+', IntType(), methodEnv.frame))
        if isLocal:
            result.append(self.emit.emitWRITEVAR(idSym.name, IntType(), index, methodEnv.frame))
        else:
            result.append(self.emit.emitPUTSTATIC(lexeme, IntType(), methodEnv.frame))
        result.append(self.emit.emitGOTO(startLabel, methodEnv.frame))

        result.append(self.emit.emitLABEL(breakLabel, methodEnv.frame))
        methodEnv.frame.exitLoop()
        methodEnv.sym = methodEnv.sym[1:]
        return ''.join(result)

    def visitWhile(self, ast, methodEnv):
        methodEnv.sym.insert(0, [])
        self.isRead = True
        result = []
        methodEnv.frame.enterLoop()
        continueLabel, breakLabel = methodEnv.frame.getContinueLabel(), methodEnv.frame.getBreakLabel()

        result.append(self.emit.emitLABEL(continueLabel, methodEnv.frame))
        self.expectType = BoolType()
        result.append(self.visit(ast.exp, methodEnv)[0])
        result.append(self.emit.emitIFFALSE(breakLabel, methodEnv.frame))

        methodEnv.frame.enterScope(False)
        tempStartLabel, tempEndLabel = methodEnv.frame.getStartLabel(), methodEnv.frame.getEndLabel()
        result.append(self.emit.emitLABEL(tempStartLabel, methodEnv.frame))
        for decl in ast.sl[0]:
            code, _ = self.visit(decl, methodEnv)
            result.append(code)

        for stmt in ast.sl[1]:
            self.isUnreachable = False
            result.append(self.visit(stmt, methodEnv))
        result.append(self.emit.emitLABEL(tempEndLabel, methodEnv.frame))
        methodEnv.frame.exitScope()

        # Neu statement cuoi cung la return, break hoac continue, khong can goto
        if not self.isUnreachable:
            result.append(self.emit.emitGOTO(continueLabel, methodEnv.frame))
            self.isUnreachable = False
        result.append(self.emit.emitLABEL(breakLabel, methodEnv.frame))
        methodEnv.frame.exitLoop()
        methodEnv.sym = methodEnv.sym[1:]
        return ''.join(result)

    def visitDowhile(self, ast, methodEnv):
        methodEnv.sym.insert(0, [])
        result = []
        methodEnv.frame.enterLoop()
        continueLabel, breakLabel = methodEnv.frame.getContinueLabel(), methodEnv.frame.getBreakLabel()
        
        methodEnv.frame.enterScope(False)
        tempStartLabel, tempEndLabel = methodEnv.frame.getStartLabel(), methodEnv.frame.getEndLabel()
        result.append(self.emit.emitLABEL(tempStartLabel, methodEnv.frame))
        for decl in ast.sl[0]:
            code, _ = self.visit(decl, methodEnv)
            result.append(code)

        for stmt in ast.sl[1]:
            self.isUnreachable = False
            result.append(self.visit(stmt, methodEnv))
        result.append(self.emit.emitLABEL(tempEndLabel, methodEnv.frame))
        methodEnv.frame.exitScope()

        # Neu statement cuoi cung la return, break hoac continue, khong can goto
        if not self.isUnreachable:
            result.append(self.emit.emitLABEL(continueLabel, methodEnv.frame)) 
            self.isUnreachable = False

        self.isRead = True
        self.expectType = BoolType()
        result.append(self.visit(ast.exp, methodEnv)[0])
        result.append(self.emit.emitIFFALSE(breakLabel, methodEnv.frame))
        result.append(self.emit.emitGOTO(tempStartLabel, methodEnv.frame))
        result.append(self.emit.emitLABEL(breakLabel, methodEnv.frame))
        methodEnv.frame.exitLoop()
        methodEnv.sym = methodEnv.sym[1:]
        return ''.join(result)

    def visitBreak(self, ast, methodEnv):
        self.isUnreachable = True
        return self.emit.emitGOTO(methodEnv.frame.getBreakLabel(), methodEnv.frame)
    
    def visitContinue(self, ast, methodEnv):
        self.isUnreachable = True
        return self.emit.emitGOTO(methodEnv.frame.getContinueLabel(), methodEnv.frame)

    def visitReturn(self, ast, methodEnv):
        self.isUnreachable = True
        if ast.expr != None:
            self.isRead = True
            expCode, returnType = self.visit(ast.expr, methodEnv)
            self.retType = returnType
            return expCode + self.emit.emitRETURN(returnType, methodEnv.frame)
        else:
            self.retType = VoidType()
            return self.emit.emitRETURN(VoidType(), methodEnv.frame)