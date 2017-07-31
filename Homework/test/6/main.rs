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
    let mut StackA = vec![]; //InfixToken
    let mut StackOut = vec![]; //PostfixToken
    let wholeLength = tokens.len();
    if wholeLength == 0 || wholeLength == 2{
        return None;
    }
    if wholeLength == 1{
        match &tokens[0]{
            &InfixToken::Operand(a) => return Some(vec![PostfixToken::Operand(a)]),
            _ => return None,
        }
    }
    let path = wholeLength -1;
    let mut bal = 0;
    for pat in 0..path{
        match &tokens[pat]{
            &InfixToken::Operand(a) =>{
                match &tokens[pat+1]{
                    &InfixToken::Operand(b) => return None,
                    &InfixToken::LeftParen => return None,
                    _ => ()
                };
            }
            &InfixToken::LeftParen =>{
                match &tokens[pat+1]{
                    &InfixToken::Operator(b) => return None,
                    &InfixToken::RightParen => return None,
                    _ => ()
                };
                bal = bal + 1;
            }
            &InfixToken::RightParen =>{
                match &tokens[pat+1]{
                    &InfixToken::Operand(b) => return None,
                    &InfixToken::LeftParen => return None,
                    _ => ()
                };
                bal = bal - 1;
            }
            &InfixToken::Operator(a) =>{
                match &tokens[pat+1]{
                    &InfixToken::Operator(b) => {println!("OPOP");return None;},
                    &InfixToken::RightParen => {println!("OP");return None;},
                    _ =>()
                }
            }
        }
    }
    let thelast = &tokens[wholeLength - 1];
    match thelast{
        &InfixToken::Operand(a) => (),
        &InfixToken::RightParen => {bal = bal - 1;},
        _ => return None,
    }
    if bal != 0{
        return None;
    }

    for val in tokens{
        match val{
            &InfixToken::Operand(a) => {StackOut.push(PostfixToken::Operand(a));println!("Op");},
            &InfixToken::LeftParen => {StackA.push(InfixToken::LeftParen);println!("LeftParen");},
            &InfixToken::RightParen =>{
                let mut get = StackA.pop().unwrap();
                while get != InfixToken::LeftParen {
                    let geta = match get{
                        InfixToken::Operator(a) => PostfixToken::Operator(a),
                        _=> return None,
                    };
                    StackOut.push(geta);
                    println!("------");
                    get = StackA.pop().unwrap(); 
                }
            }
            &InfixToken::Operator(a) =>{
                if StackA.get(0) == None{
                    StackA.push(InfixToken::Operator(a));
                }
                else{
                    let Ranka = match a{
                        Operator::Add => 1,
                        Operator::Sub => 1,
                        Operator::Mul => 2,
                        Operator::Div => 2,
                    };
                    while StackA.get(0) != None{
                        let b = StackA.pop().unwrap();
                        let Rankb = match b {
                            InfixToken::Operator(Operator::Add) => 1,
                            InfixToken::Operator(Operator::Sub) => 1,
                            InfixToken::Operator(Operator::Mul) => 2,
                            InfixToken::Operator(Operator::Div) => 2, 
                            InfixToken::LeftParen =>0,
                            InfixToken::RightParen =>0,
                            _ =>0,                      
                        }; 
                        StackA.push(b);                  
                        if Rankb >= Ranka{
                            let c = StackA.pop().unwrap();
                            let d = match &c{
                                &InfixToken::Operator(e) => e,
                                _ => Operator::Add,
                            }; 
                            StackOut.push(PostfixToken::Operator(d));                       
                        }
                        else{
                            break;
                        }
                    }
                    StackA.push(InfixToken::Operator(a));
                }
            } 
        }
    }
    if StackA.get(0) != None{
        let lenb = StackA.len();
        println!("{:?}", StackA);
        for i in 0..lenb{
            let mut stacks = StackA.pop().unwrap();
            let mut stacksb = match stacks{
                InfixToken::Operator(d) => d,
                _=> Operator::Add,
            };
            StackOut.push(PostfixToken::Operator(stacksb));
        }
    }
    return Some(StackOut);
}


fn main(){
    println!("{}","***Here are the test codes:");
    println!("{}","*Basic codes for Transforms:");
    println!("{}","Test1:");
    let x = infix_to_postfix(&[InfixToken::Operand(3),
                               InfixToken::Operator(Operator::Add),
                               InfixToken::LeftParen,
                               InfixToken::Operand(2),
                               InfixToken::Operator(Operator::Sub),
                               InfixToken::Operand(5),
                               InfixToken::RightParen,
                               InfixToken::Operator(Operator::Mul),
                               InfixToken::Operand(6),
                               InfixToken::Operator(Operator::Div),
                               InfixToken::Operand(3)]);
    let y = vec![PostfixToken::Operand(3),
                 PostfixToken::Operand(2),
                 PostfixToken::Operand(5),
                 PostfixToken::Operator(Operator::Sub),
                 PostfixToken::Operand(6),
                 PostfixToken::Operator(Operator::Mul),
                 PostfixToken::Operand(3),
                 PostfixToken::Operator(Operator::Div),
                 PostfixToken::Operator(Operator::Add)];
    println!("{}{}","result:",x == Some(y));
    println!("{}{:?}","Your answer:",x);
    println!("{}{:?}","Standard answer:",Some([PostfixToken::Operand(3),
                 PostfixToken::Operand(2),
                 PostfixToken::Operand(5),
                 PostfixToken::Operator(Operator::Sub),
                 PostfixToken::Operand(6),
                 PostfixToken::Operator(Operator::Mul),
                 PostfixToken::Operand(3),
                 PostfixToken::Operator(Operator::Div),
                 PostfixToken::Operator(Operator::Add)]));
    println!("{}","*Thank for Keyi Yuan to devote the test codes above.");
    println!("{}","----------------------------------------------");
    println!("{}","Test2:");
    let x1 = infix_to_postfix(&[InfixToken::LeftParen,
                               InfixToken::Operand(3),
                               InfixToken::Operator(Operator::Add),
                               InfixToken::LeftParen,
                               InfixToken::Operand(2),
                               InfixToken::Operator(Operator::Sub),
                               InfixToken::Operand(5),
                               InfixToken::RightParen,
                               InfixToken::Operator(Operator::Mul),
                               InfixToken::Operand(6),
                               InfixToken::Operator(Operator::Div),
                               InfixToken::Operand(3)]);
    let y1 = None;
    println!("{}{}","result:",x1 == y1);
    println!("{}{:?}","Your answer:",x1);
    println!("{}{:?}","Standard answer:",y1);
    println!("{}","*Thank for Keyi Yuan to devote the test codes above.");
    println!("{}","----------------------------------------------");
    println!("{}","Test3:");
    let x2 = infix_to_postfix(&[InfixToken::LeftParen,InfixToken::Operand(9),InfixToken::Operator(Operator::Add),InfixToken::LeftParen,InfixToken::Operand(3),InfixToken::Operator(Operator::Sub),InfixToken::Operand(1),InfixToken::RightParen,InfixToken::Operator(Operator::Mul),InfixToken::Operand(3),InfixToken::Operator(Operator::Add),InfixToken::Operand(10),InfixToken::Operator(Operator::Div),InfixToken::Operand(2),InfixToken::RightParen]);
    println!("{}{}","result:",x2 == Some(vec![PostfixToken::Operand(9), PostfixToken::Operand(3), PostfixToken::Operand(1), PostfixToken::Operator(Operator::Sub), PostfixToken::Operand(3), PostfixToken::Operator(Operator::Mul), PostfixToken::Operator(Operator::Add), PostfixToken::Operand(10), PostfixToken::Operand(2), PostfixToken::Operator(Operator::Div), PostfixToken::Operator(Operator::Add)]));
    println!("{}{:?}","Your answer:",x2);
    println!("{}{}","Standard answer:","Some([Operand(9), Operand(3), Operand(1), Operator(Sub), Operand(3), Operator(Mul), Operator(Add), Operand(10), Operand(2), Operator(Div), Operator(Add)])");
    println!("{}","*Thank for Kefei Wu and Zhenghang Zhi to devote the test codes above.");
    println!("{}","----------------------------------------------");
    println!("{}","Test4:");
    let x3 = infix_to_postfix(&[InfixToken::LeftParen,InfixToken::Operand(9),InfixToken::Operator(Operator::Mul),InfixToken::LeftParen,InfixToken::Operand(4),InfixToken::Operator(Operator::Div),InfixToken::Operand(2),InfixToken::Operator(Operator::Add),InfixToken::LeftParen,InfixToken::LeftParen,InfixToken::Operand(4),InfixToken::Operator(Operator::Div),InfixToken::Operand(2),InfixToken::Operator(Operator::Add),InfixToken::Operand(1),InfixToken::RightParen,InfixToken::Operator(Operator::Mul),InfixToken::Operand(6),InfixToken::RightParen,InfixToken::RightParen,InfixToken::RightParen]);
    println!("{}{}","result:",x3 == Some(vec![PostfixToken::Operand(9), PostfixToken::Operand(4), PostfixToken::Operand(2), PostfixToken::Operator(Operator::Div), PostfixToken::Operand(4), PostfixToken::Operand(2), PostfixToken::Operator(Operator::Div), PostfixToken::Operand(1), PostfixToken::Operator(Operator::Add), PostfixToken::Operand(6), PostfixToken::Operator(Operator::Mul), PostfixToken::Operator(Operator::Add), PostfixToken::Operator(Operator::Mul)]));
    println!("{}{:?}","Your answer:",x3);
    println!("{}{}","Standard answer:","Some([Operand(9), Operand(4), Operand(2), Operator(Div), Operand(4), Operand(2), Operator(Div), Operand(1), Operator(Add), Operand(6), Operator(Mul), Operator(Add), Operator(Mul)])");
    println!("{}","*Thank for Kefei Wu and Zhenghang Zhi to devote the test codes above.");
    println!("{}","----------------------------------------------");
    println!("{}","*The following codes are maded by Xiaoxiang - Jack Shadow and some inspiration from Yimin Tang.");
    println!("{}","Test5:");
    let x4 = infix_to_postfix(&[InfixToken::Operand(1)]);
    println!("{}{}","result:",x4 == Some(vec![PostfixToken::Operand(1)]));
    println!("{}{:?}","Your answer:",x4);
    println!("{}{}","Standard answer:","Some([Operand(1)])");
    println!("{}","----------------------------------------------");
    println!("{}","Test6:");
    let x5 = infix_to_postfix(&[InfixToken::LeftParen]);
    println!("{}{}","result:",x5 == None);
    println!("{}{:?}","Your answer:",x5);
    println!("{}{}","Standard answer:","None");
    println!("{}","----------------------------------------------");
    println!("{}","Test7:");
    let x6 = infix_to_postfix(&[InfixToken::RightParen]);
    println!("{}{}","result:",x6 == None);
    println!("{}{:?}","Your answer:",x6);
    println!("{}{}","Standard answer:","None");
    println!("{}","----------------------------------------------");
    println!("{}","Test8:");
    let x7 = infix_to_postfix(&[InfixToken::LeftParen,InfixToken::LeftParen,InfixToken::RightParen,InfixToken::RightParen]);
    println!("{}{}","result:",x7 == None);
    println!("{}{:?}","Your answer:",x7);
    println!("{}{}","Standard answer:","None");
    println!("{}","----------------------------------------------");
    println!("{}","Test9:");
    let x8 = infix_to_postfix(&[InfixToken::LeftParen,InfixToken::LeftParen]);
    println!("{}{}","result:",x8 == None);
    println!("{}{:?}","Your answer:",x8);
    println!("{}{}","Standard answer:","None");
    println!("{}","----------------------------------------------");
    println!("{}","Test10:");
    let x9 = infix_to_postfix(&[InfixToken::RightParen,InfixToken::RightParen]);
    println!("{}{}","result:",x9 == None);
    println!("{}{:?}","Your answer:",x9);
    println!("{}{}","Standard answer:","None");
    println!("{}","----------------------------------------------");
    println!("{}","Test11:");
    let x10 = infix_to_postfix(&[InfixToken::Operand(1),InfixToken::Operator(Operator::Add)]);
    println!("{}{}","result:",x10 == None);
    println!("{}{:?}","Your answer:",x10);
    println!("{}{}","Standard answer:","None");
    println!("{}","----------------------------------------------");
    println!("{}","Test12:");
    let x11 = infix_to_postfix(&[InfixToken::LeftParen,InfixToken::Operator(Operator::Add),InfixToken::RightParen]);
    println!("{}{}","result:",x11 == None);
    println!("{}{:?}","Your answer:",x11);
    println!("{}{}","Standard answer:","None");
    println!("{}","----------------------------------------------");
    println!("{}","Test13:");
    let x12 = infix_to_postfix(&[InfixToken::Operator(Operator::Add),InfixToken::RightParen]);
    println!("{}{}","result:",x12 == None);
    println!("{}{:?}","Your answer:",x12);
    println!("{}{}","Standard answer:","None");
    println!("{}","----------------------------------------------");
    println!("{}","Test14:");
    let x13 = infix_to_postfix(&[InfixToken::LeftParen,InfixToken::Operator(Operator::Add)]);
    println!("{}{}","result:",x13 == None);
    println!("{}{:?}","Your answer:",x13);
    println!("{}{}","Standard answer:","None");
    println!("{}","----------------------------------------------");
    println!("{}","Test15:");
    let x14 = infix_to_postfix(&[InfixToken::Operator(Operator::Add)]);
    println!("{}{}","result:",x14 == None);
    println!("{}{:?}","Your answer:",x14);
    println!("{}{}","Standard answer:","None");
    println!("{}","----------------------------------------------");
    println!("{}","Test16:");
    let x15 = infix_to_postfix(&[InfixToken::Operand(1),InfixToken::Operand(1)]);
    println!("{}{}","result:",x15 == None);
    println!("{}{:?}","Your answer:",x15);
    println!("{}{}","Standard answer:","None");
    println!("{}","----------------------------------------------");
    println!("{}","Test17:");
    let x16 = infix_to_postfix(&[]);
    println!("{}{}","result:",x16 == None);
    println!("{}{:?}","Your answer:",x16);
    println!("{}{}","Standard answer:","None");
    println!("{}","----------------------------------------------");
    println!("{}","Test18:");
    let x17 = infix_to_postfix(&[InfixToken::Operand(1),InfixToken::Operator(Operator::Add),InfixToken::Operand(5),InfixToken::RightParen]);
    println!("{}{}","result:",x17 == None);
    println!("{}{:?}","Your answer:",x17);
    println!("{}{}","Standard answer:","None");
    println!("{}","----------------------------------------------");
    println!("{}","Test19:");
    let x18 = infix_to_postfix(&[InfixToken::Operand(1),InfixToken::Operator(Operator::Add),InfixToken::Operand(2),InfixToken::Operator(Operator::Add),InfixToken::Operand(1),InfixToken::Operand(2),InfixToken::Operator(Operator::Add),InfixToken::Operand(1),InfixToken::Operator(Operator::Add),InfixToken::Operand(2)]);
    println!("{}{}","result:",x18 == None);
    println!("{}{:?}","Your answer:",x18);
    println!("{}{}","Standard answer:","None");
    println!("{}","----------------------------------------------");
    println!("{}","Test20:");
    let x19 = infix_to_postfix(&[InfixToken::Operand(3),
                 InfixToken::Operand(2),
                 InfixToken::Operand(5),
                 InfixToken::Operator(Operator::Sub),
                 InfixToken::Operand(6),
                 InfixToken::Operator(Operator::Mul),
                 InfixToken::Operand(3),
                 InfixToken::Operator(Operator::Div),
                 InfixToken::Operator(Operator::Add)]);
                 println!("{}{}","result:",x19 == None);
                 println!("{}{:?}","Your answer:",x19);
                 println!("{}{}","Standard answer:","None");
                 println!("{}","----------------------------------------------");
    println!("{}","******Some tips for test codes:\n1.only  test11-24 are for the return None.\n2.test8 is  designed to check your add and sub whether they are complete.\n3.test13 and test19 are designed to handle the continous Operand or continous Operator.\n4.test 11,15,17,18 are designed to handle the beginning or end has Operator(including starting with several LeftParens+Operator or ending with Operator+several RightParens).");
    println!("{}","*Thank for Jinning Su and some Julaos to discover the above test area.");
    println!("{}","----------------------------------------------");
    println!("{}","At the end:\n        Merry Christmas and Happy New Year!\n        Remember to make everyday count!");
    println!("{}","----------------------------------------------");
    println!("{}","Enjoy Rust coding.\nHappy Coding!\n                      -made in Dec.25th,2016 03:20 by Jack Shadow");
}
