import math 

class Lead:
    """Class that describes something

    Python Test 2 advanced programming! 

    Attributes:
        name: 
        staff_size:
    """
    def __init__(self, name, staff_size,
                estimated_revenue, effort_factor) -> None:
        self.name = name 
        self.staff_size = staff_size
        self.estimated_revenue = estimated_revenue
        self.effort_factor = effort_factor

        # score - 1 / (staff_size / estimated_revenue * (10 ** (digits_in_revenue - digits_in_staff_size)) * effort_factor)
        self.score = 1 / (
            self.staff_size 
            / self.estimated_revenue
            * (10 
               ** (
                   int(math.log10(abs(self.estimated_revenue))) + 1)
                    - (int(math.log10(abs(self.estimated_revenue))) + 1)
               )
            * self.effort_factor
        )
    
    def get_score(self):
        return self.score
    
    def __eq__(self, __value: object) -> bool:
        return self.score > __value.score

    def __repr__(self) -> str:
        """returns the ...

        Args:
            arg1:
                Description of the arg 

        Returns:
            none, or a dict mapping
            example:   
                {..} 

        Raises:
            none: 
        """

        return "returns a long description of the class"
    
    def __str__(self) -> None: 
        return "reuturns a smaller description"

if __name__=="__main__":
    lead = Lead("NewGame", 15, 10000, 2)