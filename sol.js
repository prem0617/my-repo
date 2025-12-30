n = 325;
temp = n;
len = 0;
while (temp > 0) {
  temp = 10;
  temp = temp % 10;
  len++;
  console.log(temp);
}
console.log(len);
