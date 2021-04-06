# Resubmission Part 1
# ----------------------------------------------------------------------------
# Charlie Taylor
# Changes for Version 2:
# Added messages to be printed when determining how many lines there are.
# Changed the error messages to be more stylized
#
# line_count.py
#
# Thornton - ICS 32 Winter 2020 [w/edits by amT Spring 2021]
# Code Example
#
# This module demonstrates a function that raises an exception and another
# function that catches it.  The program, overall, counts the number of
# lines of text in a text file, by separating the program's functionality
# into self-contained parts:
#
# * A function that takes the path to a file and returns the number of
#   lines of text in it.
#
# * A function that acts as a user interface, both taking input from the
#   user and printing output.  All user interaction happens there.
#
# * A "main" block that makes the module executable as a program.
#
# It also makes a conscious, good choice about the use of memory: rather
# than reading the entire file into memory just so we can count the number
# of lines, we instead read the file one line at a time and count the lines
# as we go.  Even though we've written more code, the program, overall, is
# probably doing roughly the same amount of work; it's just that we're doing
# a little more and the Python library is doing a little less.  But the end
# result is much better, because our program is capable of handling files of
# any size, no matter how little memory we have available to us -- unless the
# entire contents of a very large file are all on a single line (and if we
# were worried about that, we could read the file even more carefully, a
# reasonable number of characters at a time, and count newline characters).

# -- amT edit: above this is the context and below is a breakdown of the
# -- parts. Please note the '''docstrings'''. All functions and methods you
# -- build this semester need to include comments with similar levels of detail
# -- for full credit. Code is read more often than it is written. Your code
# -- should be written expecting others to read it, and hopefully use it. /amT

# count_lines_in_file() takes the path to a file and returns an
# integer specifiying the number of lines of text in that file.
#
# Notice that this function does not catch any exceptions, but that it
# still has a "try" statement with a "finally" clause.  That's because
# we're using the "finally" clause to ensure that the file is closed, if
# it was successfully opened, no matter what happens.  For example,
# any of the loop iterations -- each of which reads one line from the
# file -- could raise an exception.  If so, the file will nonetheless
# have been opened, so we'll want to ensure it gets closed.  On the other
# hand, no exception might have been raised, in which case we still want
# to be sure the file gets closed.  A "finally" clause ensures both.

# def count_lines_in_file(file_path: str) -> int:
#     '''
#     Given the path to a file, returns the number of lines of text in
#     that file, or raises exceptions in a couple of different
#     circumstances:

#     * An OSError if the file could not be opened successfully.
#     * A ValueError if the file could not be read (e.g., it was not
#       a text file, but was instead something else).
#     '''

#     the_file = None

#     try:
#         the_file = open(file_path, 'r')
#         line_count = 0

#         # A "for" loop, when used to iterate over a file, runs one loop
#         # iteration for each line of text in the file.
#         for line in the_file:
#             line_count += 1

#         if line_count < 64:
#             print('Not too many lines around here')
#         elif 65 < line_count < 256:
#             print("Now that's a good amount of lines")
#         elif line_count > 256:
#             print('Woah! Too many lines!')
#         else:
#             print('Congratulations! Your number of lines is a winner!')

#         return line_count

#     finally:
#         if the_file != None:
#             the_file.close()


# You might wonder about the docstring, which specifies that either an
# OSError or ValueError might be raised, yet the names "OSError" and
# "ValueError" do not appear in the function anywhere.  This is because
# these are the errors raised by two things that we're asking Python to
# do for us:
#
# * The built-in open() function raises an OSError whenever it's unable
#   to open the file.  (It may raise a slightly different error instead,
#   but only ones that are more specific versions of OSError.)
# * When we read from the file (in this case, when we iterate over the
#   lines using a "for" loop), that may fail if the file contains
#   something other than text.  Per the Python documentation, this will
#   always raise a ValueError (or, again, something that is a more
#   specific version of a ValueError, such as a UnicodeDecodeError).
#
# An interesting question to ask at this point is why count_lines_in_file
# doesn't catch exceptions, but instead steps aside and lets its caller
# handle them instead.  Wouldn't this function be more resilient if it
# caught the exceptions?  Shouldn't we want our functions to be more
# resilient?
#
# Think about the function's job: It takes the path to a file and returns
# the number of lines of text in that file.  And here's the important
# thing: It can't possibly know where that path came from.  This function
# might be called by the run_user_interface() function below.  But it might
# also be called from the shell, or from code in another module.  There
# might have been a human user, but there might not.  This function's role
# is best kept simple, so it shouldn't make any assumptions about what its
# callers do.
#
# -- amT edit: Easter egg. When you finish your quiz, send me an email via
# -- Canvas with the line number of this line for one extra point on this quiz.
#
# Given that, now we have to ask ourselves another question.  If this
# function doesn't assume anything about where its parameter came from,
# what can it possibly do if the parameter is the path to a file that
# doesn't exist or can't otherwise be opened?  It can't ask the user for
# another path, because there may not be a user.  It can't guess about
# what other file it might try, because there's no reasonable guess.
# All it can do is say "Well, I tried, but I failed!"  Failure to open
# the file is failure to count the number of lines in it, pure and
# simple.  In Python, that means it should step aside and let any
# exception propagate to its caller, who might be more aware of the
# broader context (e.g., is there a user?) and can, therefore, take
# appropriate action.


# This run_user_interface() function provides a simple, console-mode
# user interface that allows the user to choose a file and then
# prints how many lines of text are in the file.
#
# Here, we'll catch an exception raised by count_lines_in_file(),
# because this function is aware of the broader context.  There is a
# user and interaction is being done via the console.  So an appropriate
# thing to do might be to print an error message.

# def run_user_interface() -> None:
#     '''
#     Repeatedly asks the user to specify a file; each time, the number of
#     lines of text in the file are printed, unless the file could not be
#     opened, in which case a brief error message is displayed instead.
#     '''
#     welcome = "Welcome to the Line Counting Contraption. Version 1 by A. Thornton, and Version 2 has been made by Charlie."
#     print(welcome)
#     while True:
#         file_path = input('What file? ').strip()

#         if file_path == '':
#             break

#         try:
#             lines_in_file = count_lines_in_file(file_path)
#             print(f'{lines_in_file} line(s) in {file_path}')
#         except OSError:
#             print("Looks like we couldn't quite open that one")
#         except ValueError:
#             print("This one doesn't look like a text file to me")


# I should point out here that printing an error message to the console
# is not always what you do when you catch an exception, though it turned
# out to be reasonable enough in this example.  We'll see plenty of examples
# where something else is more appropriate.
#
# Note, too, that we've only caught the two kinds of exceptions we expect
# will be raised by count_lines_in_file: OSError and ValueError.  If anything
# else goes wrong, we're better off not catching *everything*, because then
# a bug in that function (such as misspelling the name of a variable) will
# be hidden from us beneath an opaque error message that just says "Failed".
# Better for those kinds of problems to reveal themselves with full error
# messages that tell us what's wrong, especially while we're still in the
# process of developing our program.


# if __name__ == '__main__':
#     run_user_interface()
# ----------------------------------------------------------------------------
# Resubmission Part 2
# ----------------------------------------------------------------------------
# I moved the WELCOME string from inside the run_user_interface() function to
# make it a constant, as well as move the print() for WELCOME to a main() that
# will be ran instead of just using run_user_interface(). I also added an
# assert in count_lines_in_file() to make sure that the lines were added
# correctly.
# ----------------------------------------------------------------------------
# Resubmission Part 3
# ----------------------------------------------------------------------------
WELCOME = ('Welcome to the Line Counting Contraption. Version 1 by A.' +
           'Thornton, and Version 2 has been made by Charlie.')


def count_lines_in_file(file_path: str) -> int:
    '''
    Given the path to a file, returns the number of lines of text in
    that file, or raises exceptions in a couple of different
    circumstances:

    * An OSError if the file could not be opened successfully.
    * A ValueError if the file could not be read (e.g., it was not
      a text file, but was instead something else).
    '''

    the_file = None

    try:
        the_file = open(file_path, 'r')
        line_count = 0

        # A "for" loop, when used to iterate over a file, runs one loop
        # iteration for each line of text in the file.
        for line in the_file:
            line_count += 1
        assert line_count >= 0 and type(line_count) == int
        if line_count < 64:
            print('Not too many lines around here')
        elif 65 < line_count < 256:
            print("Now that's a good amount of lines")
        elif line_count > 256:
            print('Woah! Too many lines!')
        else:
            print('Congratulations! Your number of lines is a winner!')
        return line_count
    finally:
        if the_file is not None:
            the_file.close()


def run_user_interface() -> None:
    '''
    Repeatedly asks the user to specify a file; each time, the number of
    lines of text in the file are printed, unless the file could not be
    opened, in which case a brief error message is displayed instead.
    '''
    while True:
        file_path = input('What file? ').strip()
        if file_path == '':
            break
        try:
            lines_in_file = count_lines_in_file(file_path)
            print(f'{lines_in_file} line(s) in {file_path}')
        except OSError:
            print("Looks like we couldn't quite open that one")
        except ValueError:
            print("This one doesn't look like a text file to me")


def main():
    print(WELCOME)
    run_user_interface()


if __name__ == "__main__":
    main()
# ----------------------------------------------------------------------------
