grammar BKIT;
//ID: 1813021
@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

/*--------------------------------PARSER--------------------------------------*/
program  : varDeclStm* functionDecl* EOF;
/**********Function**************/
functionDecl: FUNCTION ':' ID
                 (PARAMETER ':' paramList)?
                 BODY ':'
                    statementList
                 ENDBODY DOT;
paramList: param (CM param)*;
param: ID
      | arrayVar
      ;
/*********End Function**********/

/*********Statement************/
statementList: (varDeclStm)* (statement)* ;             // Variable decalration must appear before any other kind of statement
statement: assignmentStm
         | ifStm
         | forStm
         | whileStm
         | doWhileStm
         | callStm
         | returnStm
         | breakStm
         | continueStm
         ;

// Call statement
callStm: functionCall SC;

// Do While statement
doWhileStm: DO statementList WHILE expression ENDDO DOT;

// While statement
whileStm: WHILE expression DO statementList ENDWHILE DOT;

// For statement
forStm: FOR '(' ID ASSIGN expression ',' expression ',' expression ')' DO statementList ENDFOR DOT;

breakStm: BREAK SC;
continueStm: CONTINUE SC;
returnStm: RETURN expression? SC;

// If statement
ifStm: IF expression THEN statementList
       (ELSEIF expression THEN statementList)*
       (ELSE statementList)?
       ENDIF DOT
       ;

//Assignment statement
assignmentStm: (ID| elementExp) ASSIGN expression SC;


// Variable Declaration Statement
varDeclStm: VAR CL  varDecl  (','  varDecl )* SC;
varDecl: (arrayVar | ID) (ASSIGN literal)?;
arrayVar: ID (LS IntLit RS)+ ;

/*********End Statement************/

expression: expression1 relationalOp expression1
            | expression1;

expression1: expression1 logicalBinary expression2
             | expression2;

expression2: expression2 adding expression3
             | expression3;

expression3: expression3 multiplying expression4
             | expression4;

expression4: NOT expression4
            | expression5;

expression5:  sign expression5
            | expression6;

expression6 : LP expression RP
            | functionCall
            | elementExp
            | operand          
            ;

sign: SUB | SUBF;
multiplying: MUL|MULF|DIV|DIVF|MOD;
adding: ADD|SUB|ADDF|SUBF;
logicalBinary: AND| OR;

/*Fix here */
operand: literal | ID;

relationalOp: NEQF | GTF | STF | GEF | SEF | EQ | NEQ | GT | ST | GE | SE ;

// Index operator
elementExp:  (ID|functionCall) indexOps
            ;
indexOps: LS expression RS indexOps
        |  LS expression RS
        ;

//Function call
functionCall: ID  '(' argumentList? ')';        // Fix here
argumentList:  expression  (','  expression )*;            // argument of a function can be contant,

// Array literal
arrayLit: LB literal  (',' literal  )* RB
        ;
literal: arrayLit | IntLit | FloatLit | BoolLit | StrLit ;

//Constant: (IntLit | FloatLit | StrLit | BoolLit | ArrLit);
/*--------------------------------END PARSER--------------------------------------*/

/*--------------------------------TOKEN---------------------------------------*/
/*
 * Error
*/
ILLEGAL_ESCAPE: '"' (Escape| ~[\n'"\\])* ILLEGAL_CHAR {self.text = self.text[1:]}
                ;
UNCLOSE_STRING: '"' (Escape | ~[\n'"\\])* {self.text = self.text[1:]};

fragment ILLEGAL_CHAR:   '\\' ~('b'| 'f' | 'r' | 'n' | 't' | '\\')
                        |  '\'' ~'"'
                        | [\n']
                        ;

UNTERMINATED_COMMENT: CMTSIG ( ~'*' | '*' ~'*')*;

// Comment
Comment: CMTSIG ( ~'*' | '*' ~'*')*? CMTSIG -> skip;
fragment CMTSIG: '**';

/* String literal */
StrLit: '"' (Escape| ~[\n'"\\] )* '"' {self.text = self.text[1:-1]};
fragment Escape:  DBLQUOINSIDE | BACKSPACE | FORMFEED | CARRIAGE | NEWLINE | TAB | SINGLEQUO | BACKSLASH;
fragment DBLQUOINSIDE: '\'"';
fragment BACKSPACE: '\\b';
fragment FORMFEED: '\\f';
fragment CARRIAGE: '\\r';
fragment NEWLINE: '\\n';
fragment TAB: '\\t';
fragment SINGLEQUO: '\\\'';
fragment BACKSLASH: '\\\\';

// integer literal
IntLit: '0' | INTEGER | HEX | OCT ;

// Float literal
FloatLit: [0-9]+ DEC? EXP
        |  [0-9]+ DEC;

// Integer fragment
fragment INTEGER : [1-9][0-9]*;
fragment HEX : '0'[xX][1-9A-F][0-9A-F]*;
fragment OCT : '0'[oO][1-7][0-7]*;

// Float fragment
fragment DEC: '.'[0-9]*;
fragment EXP: [eE][+-]?[0-9]+;

/*Boolean literal */
BoolLit: TRUE | FALSE;

// Identifier
ID: [a-z][a-zA-Z0-9_]* ;
// Keyword
BODY: 'Body';
BREAK: 'Break';
CONTINUE: 'Continue';
DO : 'Do';
ELSEIF: 'ElseIf';
ENDBODY: 'EndBody';
ENDIF: 'EndIf';
ENDFOR: 'EndFor';
ENDWHILE: 'EndWhile';
FOR: 'For';
FUNCTION: 'Function';
ELSE: 'Else';
IF: 'If';
PARAMETER: 'Parameter';
RETURN: 'Return';
THEN: 'Then';
VAR: 'Var';
WHILE: 'While';
TRUE: 'True';
FALSE: 'False';
ENDDO: 'EndDo';
// Integer type Operator
ADD: '+';
SUB: '-';
MUL : '*';
DIV : '\\';
MOD : '%';
NEQ : '!=';
ST : '<';
GT: '>';
SE : '<=';
GE: '>=';

ASSIGN: '=';
EQ : '==';

// Float type operator
ADDF: '+.';
SUBF : '-.';
MULF : '*.';
DIVF : '\\.';
NEQF: '=/=';
STF: '<.';
GTF: '>.';
SEF: '<=.';
GEF: '>=.';

// Boolean operator
NOT : '!';
AND : '&&';
OR : '||';
// Seperator
LB: '{';
RB: '}';
LS: '[';
RS: ']';
CL: ':';
DOT: '.';
CM: ',';
SC: ';';
LP: '(';
RP: ')';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
ERROR_CHAR: .;
/*-----------------------------END TOKEN----------------------------------*/