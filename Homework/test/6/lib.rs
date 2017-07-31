pub enum Operator {
    // `+`
    Add,
    // `-`
    Sub,
    // `*`
    Mul,
    // `/`
    Div,
}

#[derive(Debug, PartialEq)]
pub enum InfixToken {
    Operator(Operator),
    Operand(isize),
    LeftParen,
    RightParen,
}

#[derive(Debug, PartialEq)]
pub enum PostfixToken {
    Operator(Operator),
    Operand(isize),
}

/// Transforms an infix expression to a postfix expression.
///
/// If the infix expression is valid, outputs `Some(_)`; 
/// otherwise, outputs `None`.
pub fn infix_to_postfix(tokens: &[InfixToken]) -> Option<Vec<PostfixToken>> {
    fn rank (sign1: &InfixToken, sign2: &InfixToken) -> bool {
        let mut rank1 : i32;
        let mut rank2 : i32;
        match sign1 {
            &InfixToken::Operator(Operator::Add) | &InfixToken::Operator(Operator::Sub) => {
                rank1 = 1;
            }
            &InfixToken::Operator(Operator::Mul) | &InfixToken::Operator(Operator::Div) => {
                rank1 = 2;
            }
            &LeftParen => {
                rank1 = 0;
            }
            }
        match sign2 {
            &InfixToken::Operator(Operator::Add) | &InfixToken::Operator(Operator::Sub) => {
                rank1 = 1;
            }
            &InfixToken::Operator(Operator::Mul) | &InfixToken::Operator(Operator::Div) => {
                rank1 = 2;
            }
            &InfixToken::LeftParen => {
                rank1 = 0;
            }
        }
        if (rank1 >= rank2){
            return true;
        }else{
            return false;
        }
    }

    let mut stack = vec![];
    let mut result = vec![];
    match tokens[0] {
        InfixToken::Operator(Operator) => {
            return None;
        }
        InfixToken::RightParen => {
            return None;
        }
    }
    match tokens[tokens.len()-1] {
        InfixToken::Operator(Operator) => {
            return None;
        }
        InfixToken::LeftParen => {
            return None;
        }
    }

    let mut count_l :i32 = 0;
    let mut count_r :i32 = 0;
    for i in tokens{
        match i {
            &InfixToken::LeftParen => {
                count_l = count_l + 1;
            }
            &InfixToken::RightParen => {
                count_r = count_r + 1;
            }
        }
    }
    if count_r != count_l{
        return None;
    }

    for i in 1..tokens.len()-1 {
        match tokens[i]{
            InfixToken::LeftParen => {
                match tokens[i+1] {
                    InfixToken::RightParen => {
                        return None;
                    }
                    InfixToken::Operator(Operator) => {
                        return None;
                    }
                    _ => ()
                }
                match tokens[i-1] {
                    InfixToken::RightParen => {
                        return None;
                    }
                    _ => ()
                }
            }
            InfixToken::RightParen => {
                match tokens[i+1] {
                    InfixToken::LeftParen => {
                        return None;
                    }
                    InfixToken::Operator(Operator) => {
                        return None;
                    } 
                    _ => ()
                }
                match tokens[i-1] {
                    InfixToken::LeftParen => {
                        return None;
                    }
                    InfixToken::LeftParen => {
                        return None;
                    }
                    _ => ()
                }
            }
            InfixToken::Operator(Operator) => {
                match tokens[i+1] {
                    InfixToken::Operator(Operator) => {
                        return None;
                    }
                    InfixToken::RightParen => {
                        return None;
                    }
                    _ => ()
                }
                match tokens[i-1] {
                    InfixToken::Operator(Operator) => {
                        return None;
                    }
                    InfixToken::LeftParen => {
                        return None;
                    }
                    _ => ()
                }
            }
        }
    }


    for i in tokens{
        match i {
            &InfixToken::LeftParen => {
                stack.push(i);
            }
            &InfixToken::Operator(Operator) => {
                if (stack.len() == 0){
                    stack.push(i);
                }else{
                ///如果是运算符，则比较优先级。如果当前运算符的优先级大于等于栈顶运算符的优先级(当栈顶是括号时，直接入栈)，则将运算符直接入栈；
                ///否则将栈顶运算符出栈并输出，直到当前运算符的优先级大于等于栈顶运算符的优先级(当栈顶是括号时，直接入栈)，再将当前运算符入栈。
                    let post = &stack[stack.len() - 1];
                    if (rank(i,post)){
                        stack.push(i);
                    }else{
                        while (!rank(i,stack[stack.len() - 1]) && stack.len() != 0){
                            let mid = stack.pop().unwrap();
                            result.push(mid);
                        }
                        stack.push(i);
                    }
                }
            }
            &InfixToken::Operand(a) => {
                result.push(i);
            }
            &InfixToken::RightParen => {
                while (stack[stack.len() - 1] != &InfixToken::LeftParen){
                    result.push(stack.pop().unwrap());
                }
                let m = stack.pop().unwrap();
            }
        }
    }

    let mut out = vec![];
    for i in result{
        match i {
            &InfixToken::Operand(a) => {
                let x :PostfixToken = PostfixToken::Operand(a);
                out.push(x);
            }
            &InfixToken::Operator(Operator::Add) => {
                let x :PostfixToken = PostfixToken::Operator(Operator::Add);
                out.push(x);
            }
            &InfixToken::Operator(Operator::Sub) => {
                let x :PostfixToken = PostfixToken::Operator(Operator::Sub);
                out.push(x);
            }
            &InfixToken::Operator(Operator::Mul) => {
                let x :PostfixToken = PostfixToken::Operator(Operator::Mul);
                out.push(x);
            }
            &InfixToken::Operator(Operator::Div) => {
                let x :PostfixToken = PostfixToken::Operator(Operator::Div);
                out.push(x);
            }
        }
    }
    return Some(out);
}