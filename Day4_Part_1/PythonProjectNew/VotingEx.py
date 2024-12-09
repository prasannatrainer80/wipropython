class VotingException(Exception):
    def __init__(self,message):
        self.message = message

    def __str__(self):
        return f"{self.message}"

def voting():
    age=int(input("Enter Your Age  "))
    if age < 18:
        raise VotingException("You are Not Authorized for Voting...")
    print("You Can Vote...")

try:
    voting()
except VotingException as ex:
    print(ex)