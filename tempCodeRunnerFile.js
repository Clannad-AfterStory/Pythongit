if (Date.now) {
console.log(Date.now()); // 老版本IE没有now()方法
} else {
console.log(new Date().getTime());
}