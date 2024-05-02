from javaparser import parse

def canonicalize(java_code):
  # Parse the Java code into an AST
  compilation_unit = parse(java_code)

  # Traverse the AST and rename all variables to a canonical name
  for declaration in compilation_unit.types[0].members:
    if isinstance(declaration, javaparser.tree.body.VariableDeclarator):
      declaration.name = 'var'

  # Convert the AST back into a string representation
  canonical_code = str(compilation_unit)

  return canonical_code