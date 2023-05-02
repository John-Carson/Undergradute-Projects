/*
 * Name: Jack Carson
 * Date Submitted: 1/31/22
 * Lab Section: Section 002
 * Assignment Name: 2121 Lab 2
 */

#include <stack>
#include <string>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

// Converts an infix arithmetic expression into postfix
// The function takes 3 parameters
// First parameter: array of strings for infix expression
// each string is either an integer number or operator symbol
// Second parameter: number of strings in infix expression
// Third parameter: array of strings for postfix expression
// generated by function, same format as first parameter
// assumes that postfix is at least the size of postfix
// Return value: int, number of strings in postfix expression
// Returns 0 if an error is encountered when converting expression
// An error occurs with a mismatched parenthesis, e.g. ( ( ) or ( ) ) etc.
// Operator symbols:
// ( : left parenthesis, all operations between this and ")" take place first
// ) : right parenthesis, all op.s back to previous "(" take place first
// * : multiplication, higher precedence - takes place before "+" and "-"
// / : division, higher precedence - takes place before "+" and "-"
// % : remainder, higher precedence - takes place before "+" and "-"
// + : addition, lower precedence - takes place after "*" , "/" , "%"
// - : subtraction, lower precedence - takes place after "*" , "/" , "%"
// The function is not specified to work with any other operator symbols
// Any string in infix may be assumed to be an integer operand if none
// of the above symbols

// Helper function to return precedence of present operators  
int precedence(char ch) {
   if (ch == '%' || ch == '*' || ch == '/')
      return 3;
   else if (ch == '+' || ch == '-')
      return 2;
   else
      return 1;
}

// Assigns elements of infix[] to a queue and dequeues elements
// to postfix[] in accordance with the infix to postfix algorithm
// 4 cases are handled in which the index is either "(", ")", an integer, or an operator
// The function returns the number of strings in postfix[]
int infixToPostfix(string infix[], int length, string postfix[]) {
    int i = 0;
    queue<string> queue; 
    stack<string> stack;

    // Push the infix expression into the queue
    for (int i = 0; i < length; i++) {
        queue.push(infix[i]);
    }

    // Return 0 if the number of parentheses is odd
    int count = 0; 
    for (int i = 0; i < length; i++) {
        if (infix[i] == "(" || infix[i] == ")") {
           count++;  
        }
    } if (count % 2 != 0) {
        return 0;
    }

    while (!queue.empty()) {
        
        string temp = queue.front();
        queue.pop();

        if (temp == "(") {
            stack.push(temp);
        }

        else if (temp == ")") {
            while (!stack.empty() && stack.top() != "(") {
                postfix[i] = stack.top();
                stack.pop();
                i++;
            }
            if (stack.empty()) {
                return 0;
            }
            stack.pop();
        }

        else if (temp == "+" || temp == "-" || temp == "*" || temp == "/" || temp == "%") {
            while (!stack.empty() && stack.top() != "(" && precedence(temp[0]) <= precedence(stack.top()[0])) {
                postfix[i] = stack.top();
                stack.pop();
                i++;
            }
            stack.push(temp);
        }

        else {
            postfix[i] = temp;
            i++;
        }
    }

    while (!stack.empty()) {
        postfix[i] = stack.top();
        stack.pop();
        i++;
    }

    return i; 
}

// Main function to test infixToPostfix()
// Should convert 2 + 3 * 4 + ( 5 - 6 + 7 ) * 8 to
//                2 3 4 * + 5 6 - 7 + 80 * +
int main() {
    string infixExp[] = {"2", "+", "3", "*", "4", "+", "(", "5", "-", "6", "+", "7", ")", "*", "8"};
    string postfixExp[15];
    int postfixLength;

    cout << "Infix expression: ";
    for (int i = 0; i < 15; i++) {
        cout << infixExp[i] << " ";
    }

    cout << endl;
    cout << "Length: 15" << endl << endl;

    postfixLength = infixToPostfix(infixExp, 25, postfixExp);

    cout << "Postfix expression: ";
    for (int i = 0; i < postfixLength; i++) {
        cout << postfixExp[i] << " ";
    }
    cout << endl;
    cout << "Length: " << postfixLength << endl;
    
    return 0;
}
