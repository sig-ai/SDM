#include "obj.hpp"

GameObject::GameObject() {
        this->alive = true;
        this->pos.first = 0;
        this->pos.second = 0;
        this->speed = 0;
        this->velocity.first = 0;
        this->velocity.second = 0;
}

GameObject::GameObject(int pos_x, int pos_y) : GameObject() {
        this->pos.first = pos_x;
        this->pos.second = pos_y;
}

GameObject::GameObject(int vel_x, int vel_y, int speed, int pos_x, int pos_y) : GameObject(pos_x, pos_y) {
        this->velocity.first = vel_x;
        this->velocity.second = vel_y;
}
/* Object Validity */
bool GameObject::is_alive() {
        return this->alive;
}
void GameObject::kill() {
        this->alive = false;
}

/* Object Speed */
int GameObject::get_speed() {
        return this->speed;
};

void GameObject::set_speed(int new_speed) {
        if (new_speed < 0) {
                return;
        }

        this->speed = new_speed;
};

/* Object Position */
std::pair<int,int> GameObject::get_position() {
        return this->pos;
};

void GameObject::set_position(int pos_x, int pos_y) {
        this->pos.first = pos_x;
        this->pos.second = pos_y;
}

/* Object Velocity */
std::pair<int,int> GameObject::get_velocity() {
        return this->velocity;
}

void GameObject::set_velocity(int vel_x, int vel_y) {
        this->velocity.first = vel_x;
        this->velocity.second = vel_y;
}
