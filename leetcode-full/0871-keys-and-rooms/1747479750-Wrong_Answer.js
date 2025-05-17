/**
 * @param {number[][]} rooms
 * @return {boolean}
 */
var canVisitAllRooms = function (rooms) {
    visited = []
    queue = [0]
    while (queue.length != 0) {
        let curRoom = queue.shift()
        for (let x of rooms[curRoom]) {
            if (!queue.includes(x) && !visited.includes(x)) {
                queue.push(x)
                visited.push(curRoom)
            }
        }
    }
    return visited.length == rooms.length
};
