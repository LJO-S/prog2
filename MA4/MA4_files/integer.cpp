#include <cstdlib>
// Integer class 
// Student: Ludvig Snihs
// Mail: ludvig.snihs.7653@student.uu.se
// Date: 2021-10-08
// Reviewed by: Mohammed Mosa

class Integer{
	public:
		Integer(int);
		int get();
		void set(int);
		int fib();
	private:
		int val;
		int fib_helper(int);
	};
 
Integer::Integer(int n){
	val = n;
	}
 
int Integer::get(){
	return val;
	}

void Integer::set(int n){
	val = n;
	}

int Integer::fib(){
	return fib_helper(val);
	}

int Integer::fib_helper(int n){
	if (n==1){
		return n;
	} else if (n==0){
		return n;
	} else {
		return fib_helper(n-1) + fib_helper(n-2);
	}
	}

extern "C"{
	Integer* Integer_new(int n) {return new Integer(n);}
	int Integer_get(Integer* integer) {return integer->get();}
	int Integer_fib (Integer* integer) {return integer->fib();}
	void Integer_set(Integer* integer, int n) {integer->set(n);}
	void Integer_delete(Integer* integer){
		if (integer){
			delete integer;
			integer = nullptr;
			}
		}
	}
