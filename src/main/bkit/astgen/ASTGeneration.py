from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *


class ASTGeneration(BKITVisitor):
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        """ Return program object"""
        varDecls = []
        for varDeclCtx in ctx.varDeclStm():
            varDecls += varDeclCtx.accept(self)
        funcDecls = [funcDeclCtx.accept(self) for funcDeclCtx in ctx.functionDecl()]
        decls = varDecls + funcDecls
        return Program(decls)

    def visitFunctionDecl(self, ctx:BKITParser.FunctionDeclContext):
        """ Return FuncDecl object"""
        param = ctx.paramList().accept(self) if ctx.paramList() else []
        return FuncDecl(Id(ctx.ID().getText()), param, ctx.statementList().accept(self))

    def visitParamList(self, ctx:BKITParser.ParamListContext):
        """return List[VarDecl] """
        return [paramCtx.accept(self) for paramCtx in ctx.param()]

    def visitParam(self, ctx:BKITParser.ParamContext):
        """ Return VarDecl object"""
        if ctx.ID():
            return VarDecl(Id(ctx.ID().getText()), [], None)
        else:
            id, idxs =  self.visitArrayVar(ctx.arrayVar())
            return VarDecl(Id(id), idxs, None)

    def visitStatementList(self, ctx:BKITParser.StatementListContext):
        """Return Tuple[List[VarDecl], List[Stmt]] """
        vardecls = []
        for varDeclStmCtx in ctx.varDeclStm():
            vardecls += varDeclStmCtx.accept(self);
        return (vardecls,
                [statementCtx.accept(self) for statementCtx in ctx.statement()])


    def visitStatement(self, ctx:BKITParser.StatementContext):
        """ Return Stmt object"""
        if ctx.assignmentStm():
            return ctx.assignmentStm().accept(self)
        elif ctx.ifStm():           # If statement
            return ctx.ifStm().accept(self)
        elif ctx.forStm():          # For statement
            return ctx.forStm().accept(self)
        elif ctx.whileStm():        # while statement
            return ctx.whileStm().accept(self)
        elif ctx.doWhileStm():      # do while statement
            return ctx.doWhileStm().accept(self)
        elif ctx.callStm():         # call statement
            return ctx.callStm().accept(self)
        elif ctx.returnStm():       # return statement
            return ctx.returnStm().accept(self)
        elif ctx.breakStm():        # break statement
            return ctx.breakStm().accept(self)
        else :                      # continue statement
            return ctx.continueStm().accept(self)


    def visitCallStm(self, ctx:BKITParser.CallStmContext):
        """return CallExpr object """
        callExpr = self.visitFunctionCall(ctx.functionCall())
        return CallStmt(callExpr.method, callExpr.param)

    # return DoWhle object    
    def visitDoWhileStm(self, ctx:BKITParser.DoWhileStmContext):
        """ """
        return Dowhile(ctx.statementList().accept(self), ctx.expression().accept(self))

    def visitWhileStm(self, ctx:BKITParser.WhileStmContext):
        """ return While object"""
        return While(ctx.expression().accept(self), ctx.statementList().accept(self))


    def visitForStm(self, ctx:BKITParser.ForStmContext):
        """return For object """
        return For(Id(ctx.ID().getText()), ctx.expression(0).accept(self), ctx.expression(1).accept(self),
                   ctx.expression(2).accept(self), ctx.statementList().accept(self))

    def visitBreakStm(self, ctx:BKITParser.BreakStmContext):
        """ return Break object"""
        return Break() 

    def visitContinueStm(self, ctx:BKITParser.ContinueStmContext):
        """Return Continue object"""
        return Continue()

    def visitReturnStm(self, ctx:BKITParser.ReturnStmContext):
        """ return Return object"""
        if ctx.expression():
            return Return(ctx.expression().accept(self))
        else:
            return Return(None)




    def visitIfStm(self, ctx:BKITParser.IfStmContext):
        """return If object """
        expressions = [expCtx.accept(self) for expCtx in ctx.expression()]
        # List[Tuple[List[VarDecl], List[Stm]]]
        # len(tuples) = len(expression) + 1 if "else" statement exists
        tuples  = [stmListCtx.accept(self) for stmListCtx in ctx.statementList()]
        # First if-then statement
        ifThenStmt = [(expressions[0], tuples[0][0], tuples[0][1])]
        for idx, exp in enumerate(expressions[1:]):
            ifThenStmt += [(exp, tuples[idx+1][0], tuples[idx+1][1])]
        # Else stmt
        elseStmt = None
        if ctx.ELSE():
            elseStmt = tuples[-1]
        else:
            elseStmt = ([], [])
        return If(ifThenStmt, elseStmt)


    def visitAssignmentStm(self, ctx:BKITParser.AssignmentStmContext):
        """ return Assign object"""
        lhs = None
        if ctx.ID():
            lhs = Id(ctx.ID().getText())
        else:
            lhs = ctx.elementExp().accept(self)
        return Assign(lhs, ctx.expression().accept(self))

    def visitVarDeclStm(self, ctx:BKITParser.VarDeclStmContext):
        """ return List[Vardecl]"""
        return [varDeclCtx.accept(self) for varDeclCtx in ctx.varDecl()]


    def visitVarDecl(self, ctx:BKITParser.VarDeclContext):
        """ return VarDecl object"""
        variable = None
        varDimen = []
        if ctx.ID():
            variable = Id(ctx.ID().getText())
        else:
            name, varDimen = ctx.arrayVar().accept(self)
            variable = Id(name)
        varInit = ctx.literal().accept(self) if ctx.literal() else None
        return VarDecl(variable, varDimen, varInit)

    def visitArrayVar(self, ctx:BKITParser.ArrayVarContext):
        """Return (ID, List[Int])"""
        def toInt(intStr: str):
            if intStr.startswith("0x") or intStr.startswith("0X"):
                return int(intStr, 16)
            elif intStr.startswith("0o") or intStr.startswith("0O"):
                return int(intStr, 8)
            else:
                return int(intStr, 10)
        idxs = [toInt(intLitNode.getText()) for intLitNode in ctx.IntLit()]
        return ctx.ID().getText(), idxs

    def visitExpression(self, ctx:BKITParser.ExpressionContext):
        if ctx.relationalOp():
            op = ctx.relationalOp().accept(self)
            return BinaryOp(op, ctx.expression1(0).accept(self), ctx.expression1(1).accept(self))
        else:
            return ctx.expression1(0).accept(self)


    # Visit a parse tree produced by BKITParser#expression1.
    def visitExpression1(self, ctx:BKITParser.Expression1Context):
        if ctx.logicalBinary():
            op = ctx.logicalBinary().accept(self)
            return BinaryOp(op, ctx.expression1().accept(self), ctx.expression2().accept(self))  
        else:
            return ctx.expression2().accept(self)

    # Visit a parse tree produced by BKITParser#expression2.
    def visitExpression2(self, ctx:BKITParser.Expression2Context):
        if ctx.adding():
            op = ctx.adding().accept(self)
            return BinaryOp(op, ctx.expression2().accept(self), ctx.expression3().accept(self))
        else:
            return ctx.expression3().accept(self)

    # Visit a parse tree produced by BKITParser#expression3.
    def visitExpression3(self, ctx:BKITParser.Expression3Context):
        if ctx.multiplying():
            op = ctx.multiplying().accept(self)
            return BinaryOp(op, ctx.expression3().accept(self), ctx.expression4().accept(self))
        else:
            return ctx.expression4().accept(self)

    # Visit a parse tree produced by BKITParser#expression4.
    def visitExpression4(self, ctx:BKITParser.Expression4Context):
        if ctx.NOT():
            return UnaryOp(ctx.NOT().getText(), ctx.expression4().accept(self))
        else:
            return ctx.expression5().accept(self)

    # Visit a parse tree produced by BKITParser#expression5.
    def visitExpression5(self, ctx:BKITParser.Expression5Context):
        if ctx.sign():
            return UnaryOp(ctx.sign().accept(self), ctx.expression5().accept(self))
        else:
            return ctx.expression6().accept(self)

    # Visit a parse tree produced by BKITParser#expression6.
    def visitExpression6(self, ctx:BKITParser.Expression6Context):
        if ctx.expression():
            return ctx.expression().accept(self)
        elif ctx.functionCall():
            return ctx.functionCall().accept(self)
        elif ctx.elementExp():
            return ctx.elementExp().accept(self)
        else:
            return ctx.operand().accept(self)


    def visitSign(self, ctx:BKITParser.SignContext):
        """Return text of operator"""
        return ctx.getChild(0).getText()

    
    def visitMultiplying(self, ctx:BKITParser.MultiplyingContext):
        """Return text of operator"""
        return ctx.getChild(0).getText()


    
    def visitAdding(self, ctx:BKITParser.AddingContext):
        """Return text of operator"""
        return ctx.getChild(0).getText()


   
    def visitLogicalBinary(self, ctx:BKITParser.LogicalBinaryContext):
        """Return text of operator"""
        return ctx.getChild(0).getText()


    
    def visitOperand(self, ctx:BKITParser.OperandContext):
        """Return operand object"""
        if ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return ctx.literal().accept(self)

    
    def visitRelationalOp(self, ctx:BKITParser.RelationalOpContext):
        """Return text of operator"""
        return ctx.getChild(0).getText()


    
    def visitElementExp(self, ctx:BKITParser.ElementExpContext):
        """Return ArrayCell object"""
        
        lhs = None
        if ctx.ID():
            lhs = Id(ctx.ID().getText())
        else:
            lhs = ctx.functionCall().accept(self)

        idx = ctx.indexOps().accept(self)
        return ArrayCell(lhs, idx)

    
    def visitIndexOps(self, ctx:BKITParser.IndexOpsContext):
        """Return List[Expr]"""
        if ctx.indexOps():
            return [ctx.expression().accept(self)] + ctx.indexOps().accept(self)
        else:
            return [ctx.expression().accept(self)]

    
    def visitFunctionCall(self, ctx:BKITParser.FunctionCallContext):
        """Return CallExpr object"""
        method = Id(ctx.ID().getText())
        param = []
        if ctx.argumentList():
            param = ctx.argumentList().accept(self)
        return CallExpr(method, param)


    def visitArgumentList(self, ctx:BKITParser.ArgumentListContext):
        """Return List[Expr]"""        
        exps = [expCtx.accept(self) for expCtx in ctx.expression()]
        return exps 

    def visitArrayLit(self, ctx:BKITParser.ArrayLitContext):
        """Return ArrayLiteral object"""
        literals = [litCtx.accept(self) for litCtx in ctx.literal()]
        return ArrayLiteral(literals)

    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        """Return literal object"""    
        if ctx.arrayLit():
            return ctx.arrayLit().accept(self)
        elif ctx.IntLit():
            # Util func
            def toInt(intStr: str):
                if intStr.startswith("0x") or intStr.startswith("0X"):
                    return int(intStr, 16)
                elif intStr.startswith("0o") or intStr.startswith("0O"):
                    return int(intStr, 8)
                else:
                    return int(intStr, 10)

            return IntLiteral(toInt(ctx.IntLit().getText()))
        elif ctx.FloatLit():
            return FloatLiteral(float(ctx.FloatLit().getText()))
        elif ctx.StrLit():
            return StringLiteral(ctx.StrLit().getText())
        else:
            value = True if ctx.BoolLit().getText()=="True" else False 
            return BooleanLiteral(value)