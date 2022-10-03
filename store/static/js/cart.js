let increase = 0;
document.getElementById('cartBtn').onclick = function () {
    increase += 1;
    document.getElementById('cartValue').innerHTML = increase;
}