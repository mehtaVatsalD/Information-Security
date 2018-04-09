#include<iostream>
#include<string>
#include<sstream>
using namespace std;

string msg="",msg1="";
string ipad = "0110110"; // ipad = 0x36...
string opad = "1011100"; // opad = 0x5c...
string key = "1010101"; // 7 bits of key...
string msg_hash = "";

int shf(string msg,int length) {
	int Hash = 124564352;
	int Magic = 5674356;
	int i=0;
	
	for(i=0;i<length;i++) {
		Hash = Hash ^ (msg[i]);
		Hash = Hash * Magic;
	}
	return Hash;
}

string ToHex(int input) {
	string Hexhash;
	stringstream hexstream;
	hexstream << hex << input;
	Hexhash = hexstream.str();
	return Hexhash;	
}

string int_to_str(int num) {
    stringstream ss;
    ss << num;
    return ss.str();
}

string binary(int num,string msg) {
	int binarynum[1000],i=0,j;
	while(num>0) {
		binarynum[i] = num%2;
		num = num/2;
		i++;
	}
	for(j=i-1;j>=0;j--) {
		msg += int_to_str(binarynum[j]);
	}
	return msg;
}

void generateBbits(string key,string ipad) {
	int i=0,x,y,z;
	string first_block="";
	for(i=0;i<key.length();i++) {
		x = key[i] - '0';
		y = ipad[i] - '0';
		z = x ^ y;
		first_block += int_to_str(z);
	}
	msg1 = first_block + msg1;
}

int main() {
	int i,num,b=7;
	char ch;
	// take the message from user...
	printf("Enter the messsage : ");
	cin >> msg;
	
	for(i=0;i<msg.length();i++) {
		ch = msg[i];
		//convert char into binary formate and add binary into msg1...
		num = (int)ch;
		msg1 = binary(num,msg1);
	}
	// generate 1st b bits of message...
	generateBbits(key,ipad);
	cout << msg1 << "\n";
	// create a hash function for the message...
	msg1 = ToHex(shf(msg1,msg1.length()));
	// padding to b bits...
	msg1 = msg1.substr(0,7);
	// generate 1st b bits of message...
	generateBbits(key,opad);
	// create a hash function for the message...
	msg1 = ToHex(shf(msg1,msg1.length()));
	cout << "The HMAC of a given string is : " << msg1;
	return 0;
}
