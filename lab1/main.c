#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct node {
    int id;
    char* name;
    float population;
    float latitude;
    float longitude;
    struct node* nodes;
};

struct node* handle_input(int N) {
    struct node* root = (struct node*)malloc(sizeof(struct node));
    root->nodes = (struct node*)malloc(sizeof(struct node) * N);

    for (int i = 0; i < N; ++i) {
        char buffer[100]; 
        fgets(buffer, sizeof(buffer), stdin);
        struct node* n = &root->nodes[i];
        
        char* token = strtok(buffer, " \n");
        n->id = atof(token);
        token = strtok(NULL, " ");
        n->(&name) = strdup(token);
        token = strtok(NULL, " ");
        n->population = atof(token);
        token = strtok(NULL, " ");
        n->latitude = atof(token);
        token = strtok(NULL, " ");
        n->longitude = atof(token);
        
        printf("%.2f %s %.2f %.2f %.2f\n", n->id, n->name, n->population, n->latitude, n->longitude);
    }

    return root;
}
void ignore_first_line() {
    char* str = NULL;
    size_t len = 0;
    getline(&str,&len,stdin);
    free(str);
}

int main() {
    int N = 8;

    ignore_first_line();
    struct node* root = handle_input(N);

    return 0;
}