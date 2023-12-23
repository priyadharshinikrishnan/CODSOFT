#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
    // Seed the random number generator with the current time
    std::srand(static_cast<unsigned int>(std::time(0)));

    // Generate a random number between 1 and 100
    int secretNumber = std::rand() % 100 + 1;

    // Initialize the user's guess
    int userGuess;
    int attempts = 0;

    // Welcome message
    std::cout << "Welcome to the Guess the Number game!\n";
    std::cout << "I have chosen a number between 1 and 100. Try to guess it.\n";

    // Main game loop
    do {
        // Get the user's guess
        std::cout << "Enter your guess: ";
        std::cin >> userGuess;
        attempts++;

        // Provide feedback
        if (userGuess < secretNumber) {
            std::cout << "Too low! Try again.\n";
        } else if (userGuess > secretNumber) {
            std::cout << "Too high! Try again.\n";
        } else {
            // If the guess is correct
            std::cout << "Congratulations! You guessed the number " << secretNumber << " in " << attempts << " attempts.\n";
        }
    } while (userGuess != secretNumber);

    return 0;
}
