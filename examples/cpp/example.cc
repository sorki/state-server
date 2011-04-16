#include <cstdio>
#include <cstring>

#include "state.h"

int main(int argc, char *argv[]) {
    const int sockfd = init_socket();
    char buffer[256];
    bzero(buffer, 256);

    state_update(sockfd, "testvar", "value");
    if(state_query(sockfd, "testvar", buffer) == 0)
      printf("%s", buffer);

    state_update(sockfd, "testvar", "new_value");
    if(state_query(sockfd, "testvar", buffer) == 0)
      printf("%s", buffer);

    close_socket(sockfd);
    return 0;
}
