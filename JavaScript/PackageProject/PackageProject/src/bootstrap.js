import moment from 'moment';
console.log(moment.now());
const birthday = moment('1978-01-08', 'YYYY-MM-DD');

console.log(birthday.format('dddd'));
