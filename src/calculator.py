class Calculator :
    # return the sum between 2 operands
    def mysum(self, first_operand, second_operand):
        return first_operand + second_operand

    # return the highest number between 2 operands
    def mymax(self, first_op, second_op):
        return (first_op if first_op > second_op else second_op)
      
    def myprod(self, first_operand, second_operand):
        return first_operand * second_operand
