class Solution {
public:
    bool isValid(string s) {
        stack<char> bracketStack; // Create a stack to keep track of open brackets
        
        // Iterate through the characters in the input string
        for (char c : s) {
            if (c == '(' || c == '[' || c == '{') {
                // If an open bracket is encountered, push it onto the stack
                bracketStack.push(c);
            } else {
                // If a closing bracket is encountered, check if the stack is empty or if it matches the top element
                if (bracketStack.empty() || !isMatching(bracketStack.top(), c)) {
                    return false; // Mismatched or extra closing bracket
                }
                bracketStack.pop(); // Remove the matching open bracket
            }
        }
        
        // Check if there are any open brackets left in the stack
        return bracketStack.empty();
    }
    
private:
    bool isMatching(char open, char close) {
        return (open == '(' && close == ')') || (open == '[' && close == ']') || (open == '{' && close == '}');
    }
};
