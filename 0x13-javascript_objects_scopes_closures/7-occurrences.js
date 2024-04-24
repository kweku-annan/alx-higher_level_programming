#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  const listLength = list.length;
  let i = 0;
  while (i < listLength) {
    if (list[i] === searchElement) {
      count++;
    }
    i++;
  }
  return count;
};
