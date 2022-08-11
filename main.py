from HappyApp import HappyApp
from config import _Team

def main():
    myApp = HappyApp(_Team)
    myApp.run(debug = False)

main()