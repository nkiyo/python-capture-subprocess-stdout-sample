#include <stdio.h>
#include <unistd.h>

int main() {
    printf(">> start at sub process\n");

    sleep(3);
    // TODO 子プロセスを起動する

    printf("<< end at sub process\n");
}
