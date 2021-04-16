# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#functionDecl.
    def visitFunctionDecl(self, ctx:BKITParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#paramList.
    def visitParamList(self, ctx:BKITParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#param.
    def visitParam(self, ctx:BKITParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statementList.
    def visitStatementList(self, ctx:BKITParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement.
    def visitStatement(self, ctx:BKITParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#callStm.
    def visitCallStm(self, ctx:BKITParser.CallStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#doWhileStm.
    def visitDoWhileStm(self, ctx:BKITParser.DoWhileStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#whileStm.
    def visitWhileStm(self, ctx:BKITParser.WhileStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#forStm.
    def visitForStm(self, ctx:BKITParser.ForStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#breakStm.
    def visitBreakStm(self, ctx:BKITParser.BreakStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continueStm.
    def visitContinueStm(self, ctx:BKITParser.ContinueStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#returnStm.
    def visitReturnStm(self, ctx:BKITParser.ReturnStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#ifStm.
    def visitIfStm(self, ctx:BKITParser.IfStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assignmentStm.
    def visitAssignmentStm(self, ctx:BKITParser.AssignmentStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#varDeclStm.
    def visitVarDeclStm(self, ctx:BKITParser.VarDeclStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#varDecl.
    def visitVarDecl(self, ctx:BKITParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#arrayVar.
    def visitArrayVar(self, ctx:BKITParser.ArrayVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression.
    def visitExpression(self, ctx:BKITParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression1.
    def visitExpression1(self, ctx:BKITParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression2.
    def visitExpression2(self, ctx:BKITParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression3.
    def visitExpression3(self, ctx:BKITParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression4.
    def visitExpression4(self, ctx:BKITParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression5.
    def visitExpression5(self, ctx:BKITParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression6.
    def visitExpression6(self, ctx:BKITParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#sign.
    def visitSign(self, ctx:BKITParser.SignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#multiplying.
    def visitMultiplying(self, ctx:BKITParser.MultiplyingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#adding.
    def visitAdding(self, ctx:BKITParser.AddingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#logicalBinary.
    def visitLogicalBinary(self, ctx:BKITParser.LogicalBinaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operand.
    def visitOperand(self, ctx:BKITParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#relationalOp.
    def visitRelationalOp(self, ctx:BKITParser.RelationalOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#elementExp.
    def visitElementExp(self, ctx:BKITParser.ElementExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#indexOps.
    def visitIndexOps(self, ctx:BKITParser.IndexOpsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#functionCall.
    def visitFunctionCall(self, ctx:BKITParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#argumentList.
    def visitArgumentList(self, ctx:BKITParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#arrayLit.
    def visitArrayLit(self, ctx:BKITParser.ArrayLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#literal.
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        return self.visitChildren(ctx)



del BKITParser