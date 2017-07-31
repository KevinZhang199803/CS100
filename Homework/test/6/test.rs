fn main(){
	let mut a = vec![0,1,2,3,4];
	let mut b = a.get(0);
	println!("{}", b );
	a = [];
	b = a.get(0);
	println!("{}", b);
}