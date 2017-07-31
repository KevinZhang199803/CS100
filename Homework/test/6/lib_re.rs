#[derive(Clone, Copy, Debug, PartialEq)]
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
    let mut stack = vec![];
    let mut result = vec![];
    let length = tokens.len();
    if length == 0 {
        return None;
    }
    match &tokens[0] {
        &InfixToken::Operator(a) => return None,
        &InfixToken::RightParen => return None,
        _ => ()
    }
    match &tokens[length-1] {
        &InfixToken::Operator(a) => return None,
        &InfixToken::LeftParen => return None,
        _ => ()
    }
    for i in 1..length-1 {
        match &tokens[i] {
            &InfixToken::Operator(a) => {
                match &tokens[i-1] {
                    &InfixToken::Operator(a) => return None,
                    &InfixToken::LeftParen => return None,
                    _ => ()
                }
                match &tokens[i+1] {
                    &InfixToken::Operator(a) => return None,
                    &InfixToken::RightParen => return None,
                    _ => ()
                }
            }
            &InfixToken::LeftParen => {
                match &tokens[i+1] {
                    &InfixToken::Operator(a) => return None,
                    &InfixToken::RightParen => return None,
                    _ => ()
                }
                match &tokens[i-1] {
                    &InfixToken::RightParen => return None,
                    &InfixToken::Operand(a) => return None,
                    _ => ()
                }
            }
            &InfixToken::RightParen => {
                match &tokens[i+1] {
                    &InfixToken::LeftParen => return None,
                    &InfixToken::Operand(a) => return None,
                    _ => ()
                }
                match &tokens[i-1] {
                    &InfixToken::Operator(a) => return None,
                    &InfixToken::LeftParen => return None,
                    _ => ()
                }
            }
            &InfixToken::Operand(a) => {
                match &tokens[i+1] {
                    &InfixToken::Operand(a) => return None,
                    _ => ()
                }
                match &tokens[i-1] {
                    &InfixToken::Operand(a) => return None,
                    _ => ()
                }
            }    
        }
    }
    let mut count_l = 0;
    let mut count_r = 0;
    for i in 0..length {
        match &tokens[i] {
            &InfixToken::LeftParen => count_l = count_l + 1,
            &InfixToken::RightParen => count_r = count_r + 1,
            _ => ()
        }
    }
    if count_r != count_l {
        return None;
    }
    for x in tokens {
        match x {
            &InfixToken::Operand(a) => {
                result.push(PostfixToken::Operand(a));
            }
            &InfixToken::LeftParen => {
                stack.push(InfixToken::LeftParen);
            }
            &InfixToken::Operator(a) => {
                if stack.len() == 0 {
                    stack.push(InfixToken::Operator(a));
                }else{
                    let pre = stack.pop().unwrap();
                    let mut rank1:i32;
                    let mut rank2:i32;
                    rank2 = match pre {
                        InfixToken::Operator(Operator::Add) => 1,
                        InfixToken::Operator(Operator::Sub) => 1,
                        InfixToken::Operator(Operator::Mul) => 2,
                        InfixToken::Operator(Operator::Div) => 2,
                        InfixToken::LeftParen => 0,
                        _ => 1000,
                    };
                    rank1 = match x {
                        &InfixToken::Operator(Operator::Add) => 1,
                        &InfixToken::Operator(Operator::Sub) => 1,
                        &InfixToken::Operator(Operator::Mul) => 2,
                        &InfixToken::Operator(Operator::Div) => 2,
                        _ => 1000,
                    };
                    if rank1 >= rank2 {
                        stack.push(pre);
                        stack.push(InfixToken::Operator(a));
                    }else{
                        match pre {
                            InfixToken::Operator(Operator::Add) => result.push(PostfixToken::Operator(Operator::Add)),
                            InfixToken::Operator(Operator::Sub) => result.push(PostfixToken::Operator(Operator::Sub)),
                            InfixToken::Operator(Operator::Mul) => result.push(PostfixToken::Operator(Operator::Mul)),
                            InfixToken::Operator(Operator::Div) => result.push(PostfixToken::Operator(Operator::Div)),
                            _ => ()
                        }
                        let mut judge:bool = true;
                        while judge {
                            let pre2 = stack.pop().unwrap();
                            let mut rank_2:i32;
                            rank_2 = match pre2 {
                                InfixToken::Operator(Operator::Add) => 1,
                                InfixToken::Operator(Operator::Sub) => 1,
                                InfixToken::Operator(Operator::Mul) => 2,
                                InfixToken::Operator(Operator::Div) => 2,
                                InfixToken::LeftParen => 0,
                                _ => 1000,
                            };
                            if rank1 < rank_2 {
                                let q = match pre2 {
                                    InfixToken::Operator(Operator::Add) => PostfixToken::Operator(Operator::Add),
                                    InfixToken::Operator(Operator::Sub) => PostfixToken::Operator(Operator::Sub),
                                    InfixToken::Operator(Operator::Mul) => PostfixToken::Operator(Operator::Mul),
                                    InfixToken::Operator(Operator::Div) => PostfixToken::Operator(Operator::Div),
                                    _ => PostfixToken::Operator(Operator::Add),
                                };
                                result.push(q);
                            }else{
                                stack.push(pre2);
                                stack.push(InfixToken::Operator(a));
                                judge = false;
                            }
                            if stack.len() == 0 {
                                stack.push(InfixToken::Operator(a));
                                judge = false;
                            }
                        }

                    }
                }
            }
            &InfixToken::RightParen => {
                let mut judge:bool = true;
                while judge {
                    let mid = stack.pop().unwrap();
                    let q = match mid {
                        InfixToken::Operator(Operator::Add) => PostfixToken::Operator(Operator::Add),
                        InfixToken::Operator(Operator::Sub) => PostfixToken::Operator(Operator::Sub),
                        InfixToken::Operator(Operator::Mul) => PostfixToken::Operator(Operator::Mul),
                        InfixToken::Operator(Operator::Div) => PostfixToken::Operator(Operator::Div),
                        _ => PostfixToken::Operator(Operator::Add),
                    };
                    match mid {
                        InfixToken::LeftParen => judge = false,
                        _ => result.push(q),
                    }
                }
            }
        }
    }
    return Some(result);
}
