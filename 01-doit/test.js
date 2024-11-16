function intersection(arr1, arr2) {
    const set1 = new Set(arr1);
    const set2 = new Set(arr2);

    return [...set1].filter((item) => [...set2].includes(item));  // 수정된 부분
}

// 예시
const arr1 = [1, 2, 3, 4, 5, 4, 4, 4, 4];
const arr2 = [3, 4, 5, 6, 7];
console.log(intersection(arr1, arr2)); // [3, 4, 5]


const sad = new Array(10)
for (let index = 0; index < sad.length; index++) {
    console.log('asd')
    
}