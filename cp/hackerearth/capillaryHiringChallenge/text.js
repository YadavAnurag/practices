N = 4;
arr = [ [ 1, 2, 3, 4, 5 ],
  [ 2, 4, 5, 6, 7 ],
  [ 1, 2, 3, 4, 5 ],
  [ 1, 4, 2, 2, 3 ] ];


console.log(N, arr);



function compare(a,b) {
	console.log('comparing',a,b);
	ac=0,bc=0,i=0;
	while(ac!=3 || bc!=3 ){
		console.log('running', ac, bc);
		if(i<a.length){
			
			if(a[i]>=b[i]){
				ac += 1;
			}else{
				bc += 1;
			}
			i += 1;
		}else{
			break;
		}
	}
	if(ac==3)return 0;
	else return 1;
}

console.log(arr);
newArr = arr.slice(0);
againNew = newArr.slice(0);
while(arr.length != 1){
	console.log('new assign', arr);
	arr = againNew.slice(0);
	console.log('new assigned', arr);
	againNew = []; 
	for(l=0;l<arr.length;l+=2){
		console.log('value of l',l);
		rvalue = compare(arr[l],arr[l+1])
		if(rvalue == 0){
			console.log('reomve 1',arr[l+0]);
			againNew.push(arr[0]);
			console.log('reomved 1',arr);
		}else{
			console.log('reomve 0',l,arr[l+1]);
			againNew.push(arr[1]);
			console.log('reomved 0',l,arr);
		}
	}

	console.log('final new',againNew);
}


console.log(arr, newArr);