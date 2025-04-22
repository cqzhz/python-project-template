from mytools import Tool1, Tool2
from myutils import Utils1, Utils2

def main():
    # Demonstrate mytools
    print("Using mytools:")
    tool1 = Tool1()
    tool2 = Tool2()
    tool1.foo1()  # Prints: helloworld1
    tool2.foo2()  # Prints: helloworld2

    print("\nUsing myutils:")
    utils1 = Utils1()
    utils2 = Utils2()
    utils1.bar1()  # Prints: helloutils1
    utils2.bar2()  # Prints: helloutils2

if __name__ == "__main__":
    main()