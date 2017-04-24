#ifndef _GAME_OBJ_H
#define _GAME_OBJ_H

#include <utility>

class GameObject
{
public:
	GameObject();
	GameObject(int pos_x, int pos_y);
	GameObject(int vel_x, int vel_y, int speed, int pos_x, int pos_y);

	/* Object Validity */
        bool is_alive();
	void kill();

	/* Object Speed */
        int get_speed();
        void set_speed(int new_speed);

	/* Object Position */
        std::pair<int, int> get_position();
	void set_position(int pos_x, int pos_y);

	/* Object Velocity */
	std::pair<int,int> get_velocity();
	void set_velocity(int vel_x, int vel_y);

private:
        int speed;
        bool alive;
        std::pair<int,int> pos;
	std::pair<int,int> velocity;
};

#endif
