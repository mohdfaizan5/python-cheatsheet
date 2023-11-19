Doubts:
 *Difference between modules and lib
 *Research more on slicings
 *



# Libraries:

    Generally, libraries are bits of code written by you or others can you can use in your program.
- Python allows you to share functions or features with others as “modules”.


L6: File I/O {18th dec,22}

    functions:
      open() 
        The purpose is read information from it or write info to it.
        eg;
          open("somewhere/something.txt", "w")
            *w = write #disclamer, while u run program again, it will overwrite the old data
            *by default it only r(read only)
            *a = append, which adds data by keeping the existing one.
      write()
        Which allows us to write something in the file

      close()
        Which will effectively save and close the file.
      sorted()
        It returns a sorted things
       eg:
        sorted(variable, key=student["fees"], reverse=True)
         *key tell according to what basis should we sort the file
         *reverse is used for acending or decending order.
         *


    Other approch:
        with  
            Using this automatically tells you to ur using or working with file and also closes the file auto matically
          eg:
           with open("something", "a") as file:
               file.write(f"{name}\n")

             - This is more pythonic
             - Closes file for us
             - We get to know easily, as we are working with files.

    What if we want to read files from a list.
      readlines()
        Read all things from the file and return them to me as list
       eg:
        with open("names.txt", "r") as file:
            lines = file.readlines()

            #lines is the name of variable(list)

    What if we have to store more data about anything?
      We bring .csv(comma seperated values) here in use to store related data


    Dictionary tips:
      student = {"name":name, "age":age}

    Lamda funtion
        A anonomous function, which just has no name. Why u don't need to give it a name because your only calling it once or u require it once only.
            - can it return anything
      eg:
       lamda student: student["name"]

                || is equivalent to
       
       def get_name(student):
          return student["name"]



    CSV module
     reader()
       It reads the file one by one line

     DictReader()
       This is what converts the data into dict for better usage of data

     writer()
       note = csv.writer(parameter)
       note.writerow([var1,var2])

    DictWrite()
      It opens the file rather than writing as dict keys and values


    We can also manupalate binary files(images, gifs, audio, video etc and much more)

    PIL library
