class Solution {
    public int minReorder(int n, int[][] connections) {

        Queue<Integer> visited = new LinkedList<>();
        Queue<Integer> queue = new LinkedList<>();
        queue.add(0);
        int count = 0;
        while (queue.size() > 0) {
            int cur = queue.remove();
            System.out.println(cur);
            for (int x = 0; x < n - 1; x++) {
                if (connections[x][0] == cur || connections[x][1] == cur) {
                    int ind = 0;
                    if (connections[x][0] == cur && !visited.contains(connections[x][1])&& !queue.contains(connections[x][1]) ) {
                        ind = 1;
                        count++;
                        System.out.println("flip");
                    }
                    if (!queue.contains(connections[x][ind])
                            && !visited.contains(connections[x][ind])) {
                        queue.add(connections[x][ind]);
                    }
                }
            }
            visited.add(cur);
        }

        return count;
    }
}
