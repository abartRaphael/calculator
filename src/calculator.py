class Calculator :
    # return the sum between 2 operands
    def sum(self, first_operand, second_operand):
        return first_operand + second_operand

    # return the product between 2 operands
    def prod(self, first_operand, second_operand):
        return first_operand * second_operand
      
    def mymax(self, first_op, second_op):
        return (first_op if first_op > second_op else second_op)
    