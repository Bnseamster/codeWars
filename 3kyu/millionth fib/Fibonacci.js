//Code for Codewars fibonacci problem


function fib(n){
    //string rep of number
    
    if(n == 0) return 0;
    if(n == 1) return 1;
    if(n == 2) return 1;


    n = BigInt(n)
    
    if (n <= 0){
        let nextNum;
        let arr = [BigInt(0),BigInt(1)];
        n *= BigInt(-1);

        for(let i = 0; i < n; i++){
            nextNum = arr[1] - arr[0];
            arr[1] = arr[0];
            arr[0] = nextNum;
        }
           
        return console.log(BigInt(nextNum))
    }else{
        
        let arr = [BigInt(1),BigInt(1)];
        let len = arr.length;
        let nextNum;

        for(let i = 2; i < n; i++){
            nextNum = arr[len-1] + arr[len-2];
            arr[len-2] = arr[len-1];
            arr[len-1] = nextNum;
        }
      
        return console.log(BigInt(nextNum))
    }
}



function f(n){
    n = BigInt(n);
    let Phi = (Math.sqrt(5)+1)/2;
    let phi = Phi - BigInt(1);

    let ans = (Phi**n -(BigInt(-1)*phi)**n)/BigInt(Math.sqrt(5));

    console.log(BigInt(ans))

}



f(20000)
