import time

class Template():

    def __init__(self):
        pass

    def main(self, inp):
        # code here
        return

    def main_2(self, inp):
        return self.main()

    # ----------------------#
    def run_with_timer(self, main):
        start_time = time.time()
        print("Result:", main())
        print("Execution time: %s seconds" % (time.time() - start_time))

    def timer(self, main, inp):
        start_time = time.time()
        main(inp)
        return (time.time() - start_time) 

    def run(self, main):
        print(main())

    def input_generator(self):
        # randomly generate an input
        return

    def compare_result(self, main, main_2, iteration = 10):
        """
        Compare the result of main1 and main2 method
        @main1 correct method
        @main2 alternative approach
        """            
        print(f"COMPARE RESULTS ({iteration} iterations):")
        for i in range(iteration):
            inp = self.input_generator()
            correct = main(inp)
            alter = main_2(inp)
            if alter == correct:
                print(f"Test {i}: Correct")
            else:
                print(f"Test {i}: Incorrect with input {inp}")
                print(f"The answer is {alter} while it is expected {correct}")
    
    def compare_runtime(self, main, main_2, iteration = 10):
        """
        Compare the result of main1 and main2 method
        @main1 correct method
        @main2 alternative approach
        """            
        print(f"COMPARE RUNTIME main - main2 ({iteration} iterations):")
        for i in range(iteration):
            inp = self.input_generator()
            correct_timer = self.timer(main, inp)
            alter_timer = self.timer(main_2, inp)
            
            print(f"Test {i}: {correct_timer - alter_timer}s")