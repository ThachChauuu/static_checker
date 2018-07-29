// # /*
// # / @problem:
// # /   Lexer & Parser MC Language
// # / @author:
// # /   FullName: Châu Ngọc Thạch <51303740@hcmut.edu.vn>
// # /   ID: 51303740
// # */


grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::member {
def emit(self):
    tk = self.type
    if tk == UNCLOSE_STRING:       
        result = super.emit();
        raise UncloseString(result.text);
    elif tk == ILLEGAL_ESCAPE:
        result = super.emit();
        raise IllegalEscape(result.text);
    elif tk == ERROR_CHAR:
        result = super.emit();
        raise ErrorToken(result.text); 
    else:
        return super.emit();
}

options{
	language=Python3;
}



INTTYPE: 'int' ;        // COMPLETED

BOOLTYPE: 'boolean' ;   // COMPLETED

VOIDTYPE: 'void' ;      // COMPLETED

STRINGTYPE: 'string' ;  // COMPLETED

FLOATTYPE : 'float' ;   // COMPLETED

// KEYWORDS-------------------------------------------

CONTINUE: 'continue' ;  // COMPLETED

ELSE: 'else' ;          // COMPLETED

FOR: 'for' ;            // COMPLETED

IF: 'if' ;              // COMPLETED

RETURN: 'return' ;      // COMPLETED

DO: 'do' ;              // COMPLETED

WHILE: 'while' ;        // COMPLETED


// OPERATORS---------------------------------------------

ADD: '+' ;              // COMPLETED

SUB: '-' ;              // COMPLETED

MUL: '*' ;              // COMPLETED

DIV: '/' ;              // COMPLETED

NOT: '!' ;              // COMPLETED

MOD: '%' ;              // COMPLETED

OR: '||' ;              // COMPLETED

AND: '&&' ;             // COMPLETED

NEQ: '!=' ;             // COMPLETED

EQ: '==' ;              // COMPLETED

LT: '<' ;               // COMPLETED

GT: '>' ;               // COMPLETED

LTEQ: '<=' ;            // COMPLETED

GTEQ: '>=' ;            // COMPLETED

ASSIGN: '=' ;           // COMPLETED



// SEPARATORS--------------------------------------------

LP: '(' ;               // COMPLETED

RP: ')' ;               // COMPLETED

LB: '{' ;               // COMPLETED

RB: '}' ;               // COMPLETED

LS: '[' ;               // COMPLETED

RS: ']' ;               // COMPLETED

SEMI: ';' ;             // COMPLETED

COMMA: ',' ;            // COMPLETED

CA: '\'';



BREAK: 'break' ;        // COMPLETED



// INT_LITERAL--------------------------------------------

INTLIT: [0-9]+ ;        // COMPLETED



// FLOAT_LITERAL---------------------------------------------

FLOATLIT: [0-9]+ '.' [0-9]* ([eE][+-]? [0-9]+)? 
        | [0-9]* '.' [0-9]+ ([eE][+-]? [0-9]+)? 
        | [0-9]+ ([eE][+-]? [0-9]+) ;




// STRING_LITERAL----------------------------------------------

STRING_LIT:'"'('\\''b'|'\\''f'|'\\''r'|'\\''n'|'\\''t'|'\\''"'|'\\''\\'|'\\'CA|~('\\'|'"'|'\n'|'\r'))*'"'
{
    tmp = self.text;
    chieuDai = len(tmp) -1;
    self.text = tmp[1:chieuDai];
};


// BOOLEAN_LITERAL---------------------------------------------
BOOLLIT: 'true' | 'false' ; // COMPLETED


// EXCEPTIONS

ERROR_CHAR: ('@' |'$' |'&' | '`' | '?' | '|' | '~' | '\''|'#')
{
    raise ErrorToken(self.text);
};

ILLEGAL_ESCAPE: '"'('\\'~[n"]|'\\''b'|'\\''f'|'\\''r'|'\\''n'|'\\''t'|'\\'CA|'\\''"'|'\\''\\'|'\u0060\'')*
{
    raise IllegalEscape(self.text[1:]);
};

UNCLOSE_STRING: '"'('\\''b'|'\\''f'|'\\''r'|'\\''n'|'\\''t'|'\\''"'|'\\'CA|'\\''\\'|~('\\'|'"'|'\n'|'\r'))* 
{
    raise UncloseString(self.text[1:]);
};

// COMMENTS-------------------------------------------------
CMT: ('/*'  .*?  '*/' | '//'~[\r\n]* .*?)  -> skip;

// WS : [ \b\f\r\n\t\\"CA]+ -> skip ; // skip backspace, formfeed, carriage return, newline, horizontal tab, single qupte, double quote, backslash

WS : [ \b\t\n]+ -> skip ; 

// IDENTIFIER------------------------------------------

ID: [_a-zA-Z]+([a-zA-Z0-9_])* ;       // COMPLETED


program: decls+ EOF;

decls: vardecl | funcdecl ;

vardecl: primitiveType variables SEMI ;

primitiveType: BOOLTYPE | INTTYPE | FLOATTYPE | STRINGTYPE ;

variables: variable(COMMA variable)* ;

variable: ID | (ID LS INTLIT RS) ;

functype: primitiveType | VOIDTYPE | arrPointType ;

funcdecl: functype funcname LP paramlist? RP blockstmt ;

arrPointType: primitiveType LS RS ;

funcname: ID ;

paramlist: paramdecl(COMMA paramdecl)* ;

paramdecl: (primitiveType ID) | (primitiveType ID LS RS) ;

blockstmt: LB vardeclList stmtList RB ;

vardeclList: vardecl* | ;

stmtList: stmt* | ;

stmt:   ifstmt | forstmt | dowhilestmt 
        | breakstmt | continuestmt | returnstmt 
        | exprstmt 
        | blockstmt ;

ifstmt: IF LP expr RP stmt (ELSE stmt)?;

dowhilestmt: DO stmt+ WHILE expr SEMI;

forstmt: FOR LP expr SEMI expr SEMI expr RP stmt ;

continuestmt : CONTINUE SEMI;

breakstmt: BREAK SEMI;

returnstmt: RETURN expr? SEMI ;

exprstmt: expr SEMI;

expr: expr_1 ASSIGN expr | expr_1 ;

expr_1: expr_1 OR expr_2 | expr_2 ;

expr_2: expr_2 AND expr_3 | expr_3 ;

expr_3: expr_4 (EQ | NEQ) expr_4 | expr_4;

expr_4: expr_5 (LT | GT | LTEQ | GTEQ) expr_5 | expr_5 ;

expr_5: expr_5 (ADD | SUB) expr_6 | expr_6 ;

expr_6: expr_6 (DIV | MUL | MOD) expr_7 | expr_7 ;

expr_7: (SUB | NOT) expr_7 | expr_8 ;

expr_8: expr_9 LS expr RS | expr_9 ;

expr_9: BOOLLIT | LP expr RP | INTLIT 
        | FLOATLIT | STRING_LIT
        | ID | funccall;  // A element of Array or a Function call ;


// FUNCCALL-------------------------------------------------------------

funccall: ID LP (expr(COMMA expr)* | ) RP; 

