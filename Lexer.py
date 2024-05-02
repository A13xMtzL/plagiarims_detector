from enum import IntEnum

class Tag(IntEnum):
	EOF = 65535
	ERROR = 65534
	## Operators ##
	GEQ = 258
	LEQ = 259
	NEQ = 260
	ASSIGN = 261
	MOD = 262
	## REGULAR EXPRESSIONS ##
	ID = 358
	NUMBER = 359
	STRING = 360
	TRUE = 361
	FALSE = 362
	VAR = 363

	## RESERVED WORDS JAVA ##
	ABSTRACT = 464
	ASSERT = 465
	BOOLEAN = 466
	BREAK = 467
	BYTE = 468
	CASE = 469
	CATCH = 470
	CHAR = 471
	CLASS = 472
	CONST = 473
	CONTINUE = 474
	DEFAULT = 475
	DO = 476
	DOUBLE = 477
	ELSE = 478
	ENUM = 479
	EXTENDS = 480
	FINAL = 481
	FINALLY = 482
	FLOAT = 483
	FOR = 484
	GOTO = 485
	IF = 486
	IMPLEMENTS = 487
	IMPORT = 488
	INSTANCEOF = 489
	INT = 490
	INTERFACE = 491
	LONG = 492
	NATIVE = 493
	NEW = 494
	PACKAGE = 495
	PRIVATE = 496
	PROTECTED = 497
	PUBLIC = 498
	RETURN = 499
	SHORT = 500
	STATIC = 501
	STRICTFP = 502
	SUPER = 503
	SWITCH = 504
	SYNCHRONIZED = 505
	THIS = 506
	THROW = 507
	THROWS = 508
	TRANSIENT = 509
	TRY = 510
	VOID = 511
	VOLATILE = 512
	WHILE = 513

	## RESERVED WORDS C ##
	AUTO = 514
	EXTERN = 525
	REGISTER = 532
	SIGNED = 535
	SIZEOF = 536
	STRUCT = 538
	TYPEDEF = 540
	UNION = 541
	UNSIGNED = 542
	_PACKED = 546
	
class Token:
	__tag = Tag.EOF
	__value = None
	
	def __init__(self, tagId, val = None):
		self.__tag = tagId
		self.__value = val
		
	def getTag(self):
		return self.__tag
	
	def getValue(self):
		return self.__value
		
	def __str__(self):
		if self.__tag == Tag.GEQ:
			return ">="
		elif self.__tag == Tag.LEQ:
			return "<="
		elif self.__tag == Tag.NEQ:
			return "<>"
		elif self.__tag == Tag.ASSIGN:
			return ":="
		elif self.__tag == Tag.TRUE:
			return "#t"
		elif self.__tag == Tag.FALSE:
			return "#f"
		elif self.__tag == Tag.NUMBER:
			return "Numeric"
		elif self.__tag == Tag.ID:
			return "ID"
		elif self.__tag >= Tag.VAR and self.__tag <= Tag.MOD:
			return str(self.getTag()).lower()
		elif self.__tag == Tag.STRING:
			return "String"
		elif self.__tag >= Tag.ABSTRACT and self.__tag <= Tag._PACKED:
			return str(self.getValue()).lower()
		else:
			return chr(self.__tag) 
			
class Lexer:
	__peek = ' '
	__words = {}
	__input = None

	def __init__(self, text):
		self.__input = text
		self.__peek = ' '

		self.__words["ABSTRACT"] = Token(Tag.ABSTRACT, "abstract")
		self.__words["ASSERT"] = Token(Tag.ASSERT, "assert")
		self.__words["BOOLEAN"] = Token(Tag.BOOLEAN, "boolean")
		self.__words["BREAK"] = Token(Tag.BREAK, "break")
		self.__words["BYTE"] = Token(Tag.BYTE, "byte")
		self.__words["CASE"] = Token(Tag.CASE, "case")
		self.__words["CATCH"] = Token(Tag.CATCH, "catch")
		self.__words["CHAR"] = Token(Tag.CHAR, "char")
		self.__words["CLASS"] = Token(Tag.CLASS, "class")
		self.__words["CONST"] = Token(Tag.CONST, "const")
		self.__words["CONTINUE"] = Token(Tag.CONTINUE, "continue")
		self.__words["DEFAULT"] = Token(Tag.DEFAULT, "default")
		self.__words["DO"] = Token(Tag.DO, "do")
		self.__words["DOUBLE"] = Token(Tag.DOUBLE, "double")
		self.__words["ELSE"] = Token(Tag.ELSE, "else")
		self.__words["ENUM"] = Token(Tag.ENUM, "enum")
		self.__words["EXTENDS"] = Token(Tag.EXTENDS, "extends")
		self.__words["FINAL"] = Token(Tag.FINAL, "final")
		self.__words["FINALLY"] = Token(Tag.FINALLY, "finally")
		self.__words["FLOAT"] = Token(Tag.FLOAT, "float")
		self.__words["FOR"] = Token(Tag.FOR, "for")
		self.__words["GOTO"] = Token(Tag.GOTO, "goto")
		self.__words["IF"] = Token(Tag.IF, "if")
		self.__words["IMPLEMENTS"] = Token(Tag.IMPLEMENTS, "implements")
		self.__words["IMPORT"] = Token(Tag.IMPORT, "import")
		self.__words["INSTANCEOF"] = Token(Tag.INSTANCEOF, "instanceof")
		self.__words["INT"] = Token(Tag.INT, "int")
		self.__words["INTERFACE"] = Token(Tag.INTERFACE, "interface")
		self.__words["LONG"] = Token(Tag.LONG, "long")
		self.__words["NATIVE"] = Token(Tag.NATIVE, "native")
		self.__words["NEW"] = Token(Tag.NEW, "new")
		self.__words["PACKAGE"] = Token(Tag.PACKAGE, "package")
		self.__words["PRIVATE"] = Token(Tag.PRIVATE, "private")
		self.__words["PROTECTED"] = Token(Tag.PROTECTED, "protected")
		self.__words["PUBLIC"] = Token(Tag.PUBLIC, "public")
		self.__words["RETURN"] = Token(Tag.RETURN, "return")
		self.__words["SHORT"] = Token(Tag.SHORT, "short")
		self.__words["STATIC"] = Token(Tag.STATIC, "static")
		self.__words["STRICTFP"] = Token(Tag.STRICTFP, "strictfp")
		self.__words["SUPER"] = Token(Tag.SUPER, "super")
		self.__words["SWITCH"] = Token(Tag.SWITCH, "switch")
		self.__words["SYNCHRONIZED"] = Token(Tag.SYNCHRONIZED, "synchronized")
		self.__words["THIS"] = Token(Tag.THIS, "this")
		self.__words["THROW"] = Token(Tag.THROW, "throw")
		self.__words["THROWS"] = Token(Tag.THROWS, "throws")
		self.__words["TRANSIENT"] = Token(Tag.TRANSIENT, "transient")
		self.__words["TRY"] = Token(Tag.TRY, "try")
		self.__words["VOID"] = Token(Tag.VOID, "void")
		self.__words["VOLATILE"] = Token(Tag.VOLATILE, "volatile")
		self.__words["WHILE"] = Token(Tag.WHILE, "while")	

		self.__words["AUTO"] = Token(Tag.AUTO, "auto")
		self.__words["EXTERN"] = Token(Tag.EXTERN, "extern")
		self.__words["REGISTER"] = Token(Tag.REGISTER, "register")
		self.__words["SIGNED"] = Token(Tag.SIGNED, "signed")
		self.__words["SIZEOF"] = Token(Tag.SIZEOF, "sizeof")
		self.__words["STRUCT"] = Token(Tag.STRUCT, "struct")
		self.__words["TYPEDEF"] = Token(Tag.TYPEDEF, "typedef")
		self.__words["UNION"] = Token(Tag.UNION, "union")
		self.__words["UNSIGNED"] = Token(Tag.UNSIGNED, "unsigned")
		self.__words["_PACKED"] = Token(Tag._PACKED, "_packed")

	def read(self):
		self.__peek = self.__input.read(1)
	
	def readch(self, c):
		self.read()
		if self.__peek != c:
			return False

		self.__peek = ' '
		return True

	def __skipSpaces(self):
		while True:
			if self.__peek == ' ' or self.__peek == '\t' or self.__peek == '\r' or self.__peek == '\n':
				self.read()
			else:
				break
	
	def scan(self):
		self.__skipSpaces()

		if self.__peek == '/':
			if self.readch('/'):
				while True:
					self.read()
					if self.__peek == '\n':
						self.read()
						break
					if not(self.__peek):
						break
				return self.scan()
			
		if self.__peek == '<':
			if self.readch('='):
				return Token(Tag.LEQ, "<=")
			elif self.readch('>'):
				return Token(Tag.NEQ, "<>")
			else:
				return Token(ord('<'))
		elif self.__peek == '>':
			if self.readch('='):
				return Token(Tag.GEQ, ">=")
			else:
				return Token(ord('>'))
		elif self.__peek == '#':
			if self.readch('t'):
				return Token(Tag.TRUE, "#t")
			elif self.readch('f'):
				return Token(Tag.FALSE, "#f")
			else:
				return Token(ord('#'))
		elif self.__peek == ':':
			if self.readch('='):
				#print("reading :=")
				return Token(Tag.ASSIGN, ":=")
			else:
				return Token(ord(':'))

		if self.__peek  == '"':
			val = ""
			while True:
				val = val + self.__peek
				self.read()
				if self.__peek == '"':
					break
			
			val = val + self.__peek
			self.read()
			return Token(Tag.STRING, val)

		if self.__peek.isdigit():
			val = 0
			while True:
				val = (val * 10) + int(self.__peek)
				self.read()
				if not(self.__peek.isdigit()):
					if self.__peek != '.':
						break
					self.read()
				
			return Token(Tag.NUMBER, val)

		if self.__peek.isalpha():
			val = ""
			while True:
				val = val + self.__peek.upper()
				self.read()
				if not(self.__peek.isalnum()):
					break

			if val in self.__words:
				return self.__words[val]

			w = Token(Tag.ID, val)
			self.__words[val] = Token(Tag.ID, val)
			return w

		if not(self.__peek):
			return Token(Tag.EOF)			

		token = Token(ord(self.__peek))
		self.__peek = ' ' 
		return token