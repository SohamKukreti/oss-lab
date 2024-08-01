#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX_WORDS 1000
#define MAX_WORD_LENGTH 100

void toLowerCase(char *str) {
    for(int i = 0; str[i]; i++) {
        str[i] = tolower(str[i]);
    }
}

void removePunctuation(char *word) {
    int i, j = 0;
    char cleanedWord[MAX_WORD_LENGTH];
    
    for(i = 0; word[i]; i++) {
        if(isalnum(word[i])) {
            cleanedWord[j++] = word[i];
        }
    }
    cleanedWord[j] = '\0';
    strcpy(word, cleanedWord);
}

int main() {
    char paragraph[1000];
    char words[MAX_WORDS][MAX_WORD_LENGTH];
    int frequency[MAX_WORDS] = {0};
    int wordCount = 0;

    printf("Enter a paragraph: ");
    fgets(paragraph, sizeof(paragraph), stdin);
    paragraph[strcspn(paragraph, "\n")] = '\0'; 

    char *token = strtok(paragraph, " ");
    
    while(token != NULL) {
        char word[MAX_WORD_LENGTH];
        strcpy(word, token);

        toLowerCase(word);
        removePunctuation(word);

        int found = 0;
        for(int i = 0; i < wordCount; i++) {
            if(strcmp(words[i], word) == 0) {
                frequency[i]++;
                found = 1;
                break;
            }
        }

        if(!found && word[0] != '\0') {
            strcpy(words[wordCount], word);
            frequency[wordCount]++;
            wordCount++;
        }

        token = strtok(NULL, " ");
    }

    printf("\nWord Frequencies:\n");
    for(int i = 0; i < wordCount; i++) {
        printf("%s: %d\n", words[i], frequency[i]);
    }

    return 0;
}
