#-----Libraries-----
from tkinter import *
import random
from random import randint
from fractions import Fraction
from random import randrange
from random import uniform

#start of GUI
root=Tk()

#dimensions of GUI
root.minsize(height=400,width=500)

#homepage
def homepage():

  #basic section
  def basic():
    
    #destroy objects from homepage
    home_label1.destroy()
    home_button1.destroy()
    home_button2.destroy()
    home_button3.destroy()
    
    #page 2 label 1
    basic_label1=Label(root,text='In this section you can practice your adding, subtracting and multiplying',font=('Times_New_Roman',13))
    basic_label1.place(height=30, x=15, y=0)

    #page 2 label 2
    basic_label2 = Label(text="A - Addition \nB - Subtraction \nC - Multiplication \nD - BIDMAS \n\nDon't want to play? \nE - Exit Game \n")
    basic_label2.place(height=160, x=190, y=55)

    #which topic do you want to do?
    selection = Entry(root)
    selection.place(height=30,x=155,y=200)
    
    #possible choices
    def submt():
      if selection.get() == "A":
        addition()
      elif selection.get() == "B":
        subtraction()
      elif selection.get() == "C":
        multiplication()
      elif selection.get() == "D":
        bidmas()
      else:
        back()

    #accepts which topic you want to do
    basic_button2 = Button(root,text="Submit Choice",command=submt)
    basic_button2.place(height=30,x=190,y=240)

    #addition selection
    def addition():
      
      #destroy components from topic selection page
      basic_label1.destroy()
      basic_label2.destroy()
      selection.destroy()
      basic_button1.destroy()
      basic_button2.destroy()

      #select random numbers
      num_1 = randint(0,30)
      num_2 = randint(0,30)

      #displays question
      add_label1 = Label(root, text=f"What is {num_1} + {num_2} ?\n",font=('Times_New_Roman',16))
      add_label1.place(height=30,x=190,y=75)

      #provide answer in entry box
      add_selection = Entry(root)
      add_selection.place(height=30,x=190,y=120)
      
      #accept answer and decide if it is right or wrong
      def add_submt():
        
        #correct
        if int(add_selection.get()) == num_1 + num_2:
          mark = Label(root,text="Correct! Keep on playing!\n",font=('Times_New_Roman',16))
          mark.place(height=30,x=160,y=200)
        
        #incorrect
        else:
          mark = Label(root,text=f"Incorrect, the answer is {num_1+num_2}.\n",font=('Times_New_Roman',16))
          mark.place(height=30,x=150,y=200)

        #new question will destroy old question and loop the addition function again
        def new_question():
          addition()
          mark.destroy()
        
        #back to homepage destroys current page
        def add_back():
          add_label1.destroy()
          add_button1.destroy()
          add_button2.destroy()
          add_selection.destroy()
          add_button3.destroy()
          mark.destroy()
          homepage()

        #new question button
        add_button2 = Button(root,text="New Question",command=new_question)
        add_button2.place(height=30,x=190,y=240)

        #back to homepage button
        add_button3 = Button(root,text="Back",command=add_back)
        add_button3.place(height=30,x=340,y=240)
      
      #submit answer
      add_button1 = Button(root,text="Submit",command=add_submt)
      add_button1.place(height=30,x=190,y=160)

    #subtraction selection
    def subtraction():
      
      #destroy components from topic selection page
      basic_label1.destroy()
      basic_label2.destroy()
      selection.destroy()
      basic_button1.destroy()
      basic_button2.destroy()

      #select random numbers
      num_1 = randint(0,30)
      num_2 = randint(0,30)

      #displays question
      add_label1 = Label(root, text=f"What is {num_1} - {num_2} ?\n",font=('Times_New_Roman',16))
      add_label1.place(height=30,x=190,y=75)

      #provide answer in entry box
      add_selection = Entry(root)
      add_selection.place(height=30,x=190,y=120)
      
      #accept answer and decide if it is right or wrong
      def add_submt():
        
        #correct
        if int(add_selection.get()) == num_1 - num_2:
          mark = Label(root,text="Correct! Keep on playing!\n",font=('Times_New_Roman',16))
          mark.place(height=30,x=160,y=200)
        
        #incorrect
        else:
          mark = Label(root,text=f"Incorrect, the answer is {num_1-num_2}.\n",font=('Times_New_Roman',16))
          mark.place(height=30,x=150,y=200)

        #new question will destroy old question and loop the subtraction function again
        def new_question():
          mark.destroy()
          subtraction()
        
        #back to homepage destroys current page
        def add_back():
          add_label1.destroy()
          mark.destroy()
          add_button1.destroy()
          add_button2.destroy()
          add_selection.destroy()
          add_button3.destroy()
          homepage()

        #new question button
        add_button2 = Button(root,text="New Question",command=new_question)
        add_button2.place(height=30,x=190,y=240)

        #back to homepage button
        add_button3 = Button(root,text="Back",command=add_back)
        add_button3.place(height=30,x=340,y=240)
      
      #submit answer
      add_button1 = Button(root,text="Submit",command=add_submt)
      add_button1.place(height=30,x=190,y=160)

    #multiplication selection
    def multiplication():
      
      #destroy components from topic selection page
      basic_label1.destroy()
      basic_label2.destroy()
      selection.destroy()
      basic_button1.destroy()
      basic_button2.destroy()

      #select random numbers
      num_1 = randint(0,30)
      num_2 = randint(0,30)

      #displays question
      add_label1 = Label(root, text=f"What is {num_1} x {num_2} ?\n",font=('Times_New_Roman',16))
      add_label1.place(height=30,x=190,y=75)

      #provide answer in entry box
      add_selection = Entry(root)
      add_selection.place(height=30,x=190,y=120)
      
      #accept answer and decide if it is right or wrong
      def add_submt():
        
        #correct
        if int(add_selection.get()) == num_1 * num_2:
          mark = Label(root,text="Correct! Keep on playing!\n",font=('Times_New_Roman',16))
          mark.place(height=30,x=160,y=200)
        
        #incorrect
        else:
          mark = Label(root,text=f"Incorrect, the answer is {num_1*num_2}.\n",font=('Times_New_Roman',16))
          mark.place(height=30,x=150,y=200)

        #new question will destroy old question and loop the multiplication function again
        def new_question():
          mark.destroy()
          multiplication()
        
        #back to homepage destroys current page
        def add_back():
          add_label1.destroy()
          mark.destroy()
          add_button1.destroy()
          add_button2.destroy()
          add_selection.destroy()
          add_button3.destroy()
          homepage()

        #new question button
        add_button2 = Button(root,text="New Question",command=new_question)
        add_button2.place(height=30,x=190,y=240)

        #back to homepage button
        add_button3 = Button(root,text="Back",command=add_back)
        add_button3.place(height=30,x=340,y=240)
      
      #submit answer
      add_button1 = Button(root,text="Submit",command=add_submt)
      add_button1.place(height=30,x=190,y=160)

    #bidmas selection
    def bidmas():
      
      #destroy components from topic selection page
      basic_label1.destroy()
      basic_label2.destroy()
      selection.destroy()
      basic_button1.destroy()
      basic_button2.destroy()

      #select random numbers
      num_1 = randint(0,30)
      num_2 = randint(0,30)
      num_3 = randint(0,30)

      #displays question
      add_label1 = Label(root, text=f"What is {num_1} + {num_2} x {num_3} ?\n",font=('Times_New_Roman',16))
      add_label1.place(height=30,x=190,y=75)

      #provide answer in entry box
      add_selection = Entry(root)
      add_selection.place(height=30,x=190,y=120)
      
      #accept answer and decide if it is right or wrong
      def add_submt():
        
        #correct
        if int(add_selection.get()) == num_1 + num_2 * num_3:
          mark = Label(root,text="Correct! Keep on playing!\n",font=('Times_New_Roman',16))
          mark.place(height=30,x=160,y=200)
        
        #incorrect
        else:
          mark = Label(root,text=f"Incorrect, the answer is {num_1+num_2*num_3}.\n",font=('Times_New_Roman',16))
          mark.place(height=30,x=150,y=200)

        #new question will destroy old question and loop the bidmas function again
        def new_question():
          mark.destroy()
          bidmas()
        
        #back to homepage destroys current page
        def add_back():
          add_label1.destroy()
          mark.destroy()
          add_button1.destroy()
          add_button2.destroy()
          add_selection.destroy()
          add_button3.destroy()
          homepage()

        #new question button
        add_button2 = Button(root,text="New Question",command=new_question)
        add_button2.place(height=30,x=190,y=240)

        #back to homepage button
        add_button3 = Button(root,text="Back",command=add_back)
        add_button3.place(height=30,x=340,y=240)
      
      #submit answer
      add_button1 = Button(root,text="Submit",command=add_submt)
      add_button1.place(height=30,x=190,y=160)
    
    #destroy objects from basic and recreate homepage
    def back():
      basic_label1.destroy()
      basic_label2.destroy()
      basic_button1.destroy()
      selection.destroy()
      basic_button2.destroy()
      homepage()
    
    #basic page button
    basic_button1=Button(root,text='Back',font=('Times_New_Roman',14),command=back,activebackground='blue')
    
    #location of basic page button
    basic_button1.place(height=30,x=220,y=270)

  #intermediate section
  def intermediate():
    
    #destroy objects from homepage
    home_label1.destroy()
    home_button1.destroy()
    home_button2.destroy()
    home_button3.destroy()
    
    #page 2 label 1
    intermediate_label1=Label(root,text='In this section you can practice fractions',font=('Times_New_Roman',13))
    intermediate_label1.place(height=30, x=15, y=0)

    #page 2 label 2
    intermediate_label2 = Label(text="A - Adding Fractions \nB - Subtracting Fractions \nC - Multiplying Fractions \nD - Comparing Fractions\n\nDon't want to play? \nE - Exit Game \n")
    intermediate_label2.place(height=140, x=190, y=75)

    #which topic do you want to do?
    selection = Entry(root)
    selection.place(height=30,x=180,y=200)
    
    def reduce_fraction(n, d):
      def gcd(n, d):
        while d != 0:
          t = d
          d = n%d
          n = t
        return n
        assert d!=0, "integer division by zero"
        assert isinstance(d, int), "must be int"
        assert isinstance(n, int), "must be int"
        greatest=gcd(n,d)
        n/=greatest
        d/=greatest
        return n, d

    #possible choices
    def submt():
      if selection.get() == "A":
        adding_fractions()
      elif selection.get() == "B":
        subtracting_fractions()
      elif selection.get() == "C":
        multiplying_fractions()
      elif selection.get() == "D":
        comparing_fractions()
      else:
        back()

    #accepts which topic you want to do
    intermediate_button2 = Button(root,text="Submit Choice",command=submt)
    intermediate_button2.place(height=30,x=180,y=230)

    #addition selection
    def adding_fractions():
      
      #destroy components from topic selection page
      intermediate_label1.destroy()
      intermediate_label2.destroy()
      selection.destroy()
      intermediate_button1.destroy()
      intermediate_button2.destroy()

      #select random numbers
      num_1 = randint(1,15)
      num_2 = randint(2,15)
      num_3 = randint(1,15)
      num_4 = randint(2,15)

      #displays question
      add_label1 = Label(root, text=f"What is {Fraction(num_1,num_2)} + {Fraction(num_3,num_4)} ?\nHint: Remember to simplify your answer!",font=('Times_New_Roman',16))
      add_label1.place(height=60,x=150,y=65)

      #add simplify label?

      answer = Fraction(num_1,num_2)+Fraction(num_3,num_4)
      n = answer.numerator
      d = answer.denominator
      reduce_fraction(n,d)
      reduced_answer = Fraction(n,d)

      #provide answer in entry box
      add_selection = Entry(root)
      add_selection.place(height=30,x=190,y=120)
      
      #accept answer and decide if it is right or wrong
      def add_submt():
        
        #correct
        if Fraction(add_selection.get()) == reduced_answer:
          mark = Label(root,text="Correct! Keep on playing!\n",font=('Times_New_Roman',16))
          mark.place(height=30,x=160,y=200)
        
        #incorrect
        else:
          mark = Label(root,text=f"Incorrect, the answer is {reduced_answer}.\n",font=('Times_New_Roman',16))
          mark.place(height=30,x=150,y=200)

        #new question will destroy old question and loop the addition function again
        def new_question():
          mark.destroy()
          adding_fractions()
        
        #back to homepage destroys current page
        def add_back():
          add_label1.destroy()
          mark.destroy()
          add_button1.destroy()
          add_button2.destroy()
          add_selection.destroy()
          add_button3.destroy()
          homepage()

        #new question button
        add_button2 = Button(root,text="New Question",command=new_question)
        add_button2.place(height=30,x=190,y=240)

        #back to homepage button
        add_button3 = Button(root,text="Back",command=add_back)
        add_button3.place(height=30,x=340,y=240)
      
      #submit answer
      add_button1 = Button(root,text="Submit",command=add_submt)
      add_button1.place(height=30,x=190,y=160)

    #subtraction selection
    def subtracting_fractions():
      
      #destroy components from topic selection page
      intermediate_label1.destroy()
      intermediate_label2.destroy()
      selection.destroy()
      intermediate_button1.destroy()
      intermediate_button2.destroy()

      #select random numbers
      num_1 = randint(1,15)
      num_2 = randint(2,15)
      num_3 = randint(1,15)
      num_4 = randint(2,15)

      #displays question
      add_label1 = Label(root, text=f"What is {Fraction(num_1,num_2)} - {Fraction(num_3,num_4)} ?\nHint: Remember to simplify your answer!",font=('Times_New_Roman',16))
      add_label1.place(height=60,x=150,y=65)

      #add simplify label?

      answer = Fraction(num_1,num_2)-Fraction(num_3,num_4)
      n = answer.numerator
      d = answer.denominator
      reduce_fraction(n,d)
      reduced_answer = Fraction(n,d)

      #provide answer in entry box
      add_selection = Entry(root)
      add_selection.place(height=30,x=190,y=120)
      
      #accept answer and decide if it is right or wrong
      def add_submt():
        
        #correct
        if Fraction(add_selection.get()) == reduced_answer:
          mark = Label(root,text="Correct! Keep on playing!\n",font=('Times_New_Roman',16))
          mark.place(height=30,x=160,y=200)
        
        #incorrect
        else:
          mark = Label(root,text=f"Incorrect, the answer is {reduced_answer}.\n",font=('Times_New_Roman',16))
          mark.place(height=30,x=150,y=200)

        #new question will destroy old question and loop the addition function again
        def new_question():
          mark.destroy()
          subtracting_fractions()
        
        #back to homepage destroys current page
        def add_back():
          add_label1.destroy()
          mark.destroy()
          add_button1.destroy()
          add_button2.destroy()
          add_selection.destroy()
          add_button3.destroy()
          homepage()

        #new question button
        add_button2 = Button(root,text="New Question",command=new_question)
        add_button2.place(height=30,x=190,y=240)

        #back to homepage button
        add_button3 = Button(root,text="Back",command=add_back)
        add_button3.place(height=30,x=340,y=240)
      
      #submit answer
      add_button1 = Button(root,text="Submit",command=add_submt)
      add_button1.place(height=30,x=190,y=160)

    #multiplication selection
    def multiplying_fractions():
      
      #destroy components from topic selection page
      intermediate_label1.destroy()
      intermediate_label2.destroy()
      selection.destroy()
      intermediate_button1.destroy()
      intermediate_button2.destroy()

      #select random numbers
      num_1 = randint(1,15)
      num_2 = randint(2,15)
      num_3 = randint(1,15)
      num_4 = randint(2,15)

      #displays question
      add_label1 = Label(root, text=f"What is {Fraction(num_1,num_2)} x {Fraction(num_3,num_4)} ?\nHint: Remember to simplify your answer!",font=('Times_New_Roman',16))
      add_label1.place(height=60,x=150,y=65)

      #add simplify label?

      answer = Fraction(num_1,num_2)*Fraction(num_3,num_4)
      n = answer.numerator
      d = answer.denominator
      reduce_fraction(n,d)
      reduced_answer = Fraction(n,d)

      #provide answer in entry box
      add_selection = Entry(root)
      add_selection.place(height=30,x=190,y=120)
      
      #accept answer and decide if it is right or wrong
      def add_submt():
        
        #correct
        if Fraction(add_selection.get()) == reduced_answer:
          mark = Label(root,text="Correct! Keep on playing!\n",font=('Times_New_Roman',16))
          mark.place(height=30,x=160,y=200)
        
        #incorrect
        else:
          mark = Label(root,text=f"Incorrect, the answer is {reduced_answer}.\n",font=('Times_New_Roman',16))
          mark.place(height=30,x=150,y=200)

        #new question will destroy old question and loop the addition function again
        def new_question():
          mark.destroy()
          multiplying_fractions()
        
        #back to homepage destroys current page
        def add_back():
          add_label1.destroy()
          mark.destroy()
          add_button1.destroy()
          add_button2.destroy()
          add_selection.destroy()
          add_button3.destroy()
          homepage()

        #new question button
        add_button2 = Button(root,text="New Question",command=new_question)
        add_button2.place(height=30,x=190,y=240)

        #back to homepage button
        add_button3 = Button(root,text="Back",command=add_back)
        add_button3.place(height=30,x=340,y=240)
      
      #submit answer
      add_button1 = Button(root,text="Submit",command=add_submt)
      add_button1.place(height=30,x=190,y=160)

    #comparing fractions selection
    def comparing_fractions():
      
      #destroy components from topic selection page
      intermediate_label1.destroy()
      intermediate_label2.destroy()
      selection.destroy()
      intermediate_button1.destroy()
      intermediate_button2.destroy()

      #select random numbers
      num_1 = randint(1,15)
      num_2 = randint(2,15)
      num_3 = randint(1,15)
      num_4 = randint(2,15)

      #displays question
      add_label1 = Label(root, text=f"Is {Fraction(num_1,num_2)} < {Fraction(num_3,num_4)} ?\nInput True or False.",font=('Times_New_Roman',16))
      add_label1.place(height=60,x=190,y=65)

      #add simplify label?

      answer = Fraction(num_1,num_2)<Fraction(num_3,num_4)

      #provide answer in entry box
      add_selection = Entry(root)
      add_selection.place(height=30,x=190,y=120)
      
      #accept answer and decide if it is right or wrong
      def add_submt():
        
        #correct
        if str(add_selection.get()) == str(answer):
          mark = Label(root,text="Correct! Keep on playing!\n",font=('Times_New_Roman',16))
          mark.place(height=30,x=160,y=200)
        
        #incorrect
        else:
          mark = Label(root,text=f"Incorrect, the answer is {answer}.\n",font=('Times_New_Roman',16))
          mark.place(height=30,x=150,y=200)

        #new question will destroy old question and loop the addition function again
        def new_question():
          mark.destroy()
          comparing_fractions()
        
        #back to homepage destroys current page
        def add_back():
          add_label1.destroy()
          mark.destroy()
          add_button1.destroy()
          add_button2.destroy()
          add_selection.destroy()
          add_button3.destroy()
          homepage()

        #new question button
        add_button2 = Button(root,text="New Question",command=new_question)
        add_button2.place(height=30,x=190,y=240)

        #back to homepage button
        add_button3 = Button(root,text="Back",command=add_back)
        add_button3.place(height=30,x=340,y=240)
      
      #submit answer
      add_button1 = Button(root,text="Submit",command=add_submt)
      add_button1.place(height=30,x=190,y=160)
    
    #destroy objects from basic and recreate homepage
    def back():
      intermediate_label1.destroy()
      intermediate_label2.destroy()
      intermediate_button1.destroy()
      selection.destroy()
      intermediate_button2.destroy()
      homepage()
    
    #basic page button
    intermediate_button1=Button(root,text='Back',font=('Times_New_Roman',14),command=back,activebackground='blue')
    
    #location of basic page button
    intermediate_button1.place(height=30,x=220,y=270)

  #hard section
  def hard():
    
    #destroy objects from homepage
    home_label1.destroy()
    home_button1.destroy()
    home_button2.destroy()
    home_button3.destroy()
    
    #page 2 label 1
    hard_label1=Label(root,text='In this section you can practice your problem solving skills',font=('Times_New_Roman',13))
    hard_label1.place(height=30, x=15, y=0)

    #page 2 label 2
    hard_label2 = Label(text="A - Money Problems \nB - Weights \nC - Recipes \n\nDon't want to play? \nD - Exit Game \n")
    hard_label2.place(height=140, x=190, y=75)

    #which topic do you want to do?
    selection = Entry(root)
    selection.place(height=30,x=180,y=200)
    
    #possible choices
    def submt():
      if selection.get() == "A":
        money()
      elif selection.get() == "B":
        weight()
      elif selection.get() == "C":
        recipe()
      else:
        back()

    #accepts which topic you want to do
    hard_button2 = Button(root,text="Submit Choice",command=submt)
    hard_button2.place(height=30,x=180,y=230)

    #money selection
    def money():
      
      #destroy components from topic selection page
      hard_label1.destroy()
      hard_label2.destroy()
      selection.destroy()
      hard_button1.destroy()
      hard_button2.destroy()

      #select random numbers
      num_1 = round(random.uniform(1,30))
      num_2 = round(random.uniform(1,30))
      num_3 = round(random.uniform(65,100))

      #displays question
      add_label1 = Label(root, text=f"I buy a shirt costing £{num_1} and a pair of jeans costing £{num_2},\nI give the cashier £{num_3}, how much change do I recieve?\nNote: Just enter the number not the £ sign!",font=('Times_New_Roman',16))
      add_label1.place(height=70,x=70,y=55)

      #add simplify label?

      change = num_3 - num_1 - num_2

      #provide answer in entry box
      add_selection = Entry(root)
      add_selection.place(height=30,x=190,y=120)
      
      #accept answer and decide if it is right or wrong
      def add_submt():
        
        #correct
        if int(add_selection.get()) == change:
          mark = Label(root,text="Correct! Keep on playing!\n",font=('Times_New_Roman',16))
          mark.place(height=30,x=160,y=200)
        
        #incorrect
        else:
          mark = Label(root,text=f"Incorrect, the answer is £{change}.\n",font=('Times_New_Roman',16))
          mark.place(height=30,x=150,y=200)

        #new question will destroy old question and loop the addition function again
        def new_question():
          mark.destroy()
          money()
        
        #back to homepage destroys current page
        def add_back():
          add_label1.destroy()
          mark.destroy()
          add_button1.destroy()
          add_button2.destroy()
          add_selection.destroy()
          add_button3.destroy()
          homepage()

        #new question button
        add_button2 = Button(root,text="New Question",command=new_question)
        add_button2.place(height=30,x=190,y=240)

        #back to homepage button
        add_button3 = Button(root,text="Back",command=add_back)
        add_button3.place(height=30,x=340,y=240)
      
      #submit answer
      add_button1 = Button(root,text="Submit",command=add_submt)
      add_button1.place(height=30,x=190,y=160)

    #subtraction selection
    def weight():
      
      #destroy components from topic selection page
      hard_label1.destroy()
      hard_label2.destroy()
      selection.destroy()
      hard_button1.destroy()
      hard_button2.destroy()

      #select random numbers
      num_1 = round(random.uniform(1,6),2)
      num_2 = round(random.uniform(1,12),2)

      #displays question
      add_label1 = Label(root, text=f"My cat weighs {num_1}kg and my dog weighs {num_2}kg.\nHow much is their combined weight?\n",font=('Times_New_Roman',16))
      add_label1.place(height=50,x=100,y=75)

      final_weight = round(num_1 + num_2,2)

      
      #provide answer in entry box
      add_selection = Entry(root)
      add_selection.place(height=30,x=190,y=120)
      
      #accept answer and decide if it is right or wrong
      def add_submt():
        
        #correct
        if float(add_selection.get()) == final_weight:
          mark = Label(root,text="Correct! Keep on playing!\n",font=('Times_New_Roman',16))
          mark.place(height=30,x=160,y=200)
        
        #incorrect
        else:
          mark = Label(root,text=f"Incorrect, the answer is {final_weight}.\n",font=('Times_New_Roman',16))
          mark.place(height=30,x=150,y=200)

        #new question will destroy old question and loop the addition function again
        def new_question():
          mark.destroy()
          weight()
        
        #back to homepage destroys current page
        def add_back():
          add_label1.destroy()
          mark.destroy()
          add_button1.destroy()
          add_button2.destroy()
          add_selection.destroy()
          add_button3.destroy()
          homepage()

        #new question button
        add_button2 = Button(root,text="New Question",command=new_question)
        add_button2.place(height=30,x=190,y=240)

        #back to homepage button
        add_button3 = Button(root,text="Back",command=add_back)
        add_button3.place(height=30,x=340,y=240)
      
      #submit answer
      add_button1 = Button(root,text="Submit",command=add_submt)
      add_button1.place(height=30,x=190,y=160)

    #multiplication selection
    def recipe():
      
      #destroy components from topic selection page
      hard_label1.destroy()
      hard_label2.destroy()
      selection.destroy()
      hard_button1.destroy()
      hard_button2.destroy()

      #select random numbers
      num_1 = randrange(12,60,6)

      #displays question
      add_label1 = Label(root, text=f"To make 6 small sponge cakes, you will need:\n50g soft margarine\n50g caster sugar\n1 egg\n50g self-raising flour\n1 tablespoon cocoa\n6 paper cake cases\nHow many grams of self-raising flour will I need to make {num_1} cakes?\n",font=('Times_New_Roman',15))
      add_label1.place(height=160,x=5,y=10)

      multiplier = int(num_1/6)

      self_answer = int(multiplier * 50)

      #provide answer in entry box
      add_selection = Entry(root)
      add_selection.place(height=30,x=140,y=170)
      
      #accept answer and decide if it is right or wrong
      def add_submt():
        
        #correct
        if int(add_selection.get()) == self_answer:
          mark = Label(root,text="Correct! Keep on playing!\n",font=('Times_New_Roman',16))
          mark.place(height=30,x=160,y=200)
        
        #incorrect
        else:
          mark = Label(root,text=f"Incorrect.\nTo make {num_1} small sponge cakes, you will need:\n{self_answer} grams of self-raising flour",font=('Times_New_Roman',16))
          mark.place(height=90,x=70,y=270)

        #new question will destroy old question and loop the addition function again
        def new_question():
          mark.destroy()
          recipe()
        
        #back to homepage destroys current page
        def add_back():
          add_label1.destroy()
          mark.destroy()
          add_button1.destroy()
          add_button2.destroy()
          add_selection.destroy()
          add_button3.destroy()
          homepage()

        #new question button
        add_button2 = Button(root,text="New Question",command=new_question)
        add_button2.place(height=30,x=140,y=240)

        #back to homepage button
        add_button3 = Button(root,text="Back",command=add_back)
        add_button3.place(height=30,x=270,y=240)
      
      #submit answer
      add_button1 = Button(root,text="Submit",command=add_submt)
      add_button1.place(height=30,x=190,y=200)
 
    #destroy objects from basic and recreate homepage
    def back():
      hard_label1.destroy()
      hard_label2.destroy()
      hard_button1.destroy()
      selection.destroy()
      hard_button2.destroy()
      homepage()
    
    #basic page button
    hard_button1=Button(root,text='Back',font=('Times_New_Roman',14),command=back,activebackground='blue')
    
    #location of basic page button
    hard_button1.place(height=30,x=220,y=270)

  #homepage label
  home_label1=Label(root,text='Welcome to Math Practice!',font=('Times_New_Roman',18))
  
  #location of homepage label (default pack argument is top)
  home_label1.pack()

  #homepage button 1
  home_button1=Button(root,text='Basic Arithmetic',font=('Times_New_Roman',14),command=basic,activebackground='blue')
  
  #location of homepage button 1 
  home_button1.place(height=30, x=170, y=75)

  #homepage button 2
  home_button2=Button(root,text='Fractions',font=('Times_New_Roman',14),command=intermediate,activebackground='blue')

  #location of homepage button 2
  home_button2.place(height=30,x=195,y=125)

  #homepage button 3
  home_button3=Button(root,text='Problem Solving',font=('Times_New_Roman',14),command=hard,activebackground='blue')

  #location of homepage button 3
  home_button3.place(height=30,x=170,y=175)

#first thing we want to run in the app is the homepage
homepage()

#end of GUI
root.mainloop()
