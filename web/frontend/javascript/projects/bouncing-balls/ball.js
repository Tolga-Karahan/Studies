import { random, randomRGB } from './utils.js';

class Ball {
    constructor(x, y, velX, velY, color, size, ctx) {
        this.x = x;
        this.y = y;
        this.velX = velX;
        this.velY = velY;
        this.color = color;
        this.size = size;
        this.ctx = ctx;
    }

    draw() {
        this.ctx.beginPath();
        this.ctx.fillStyle = this.color;
        this.ctx.arc(this.x, this.y, this.size, 0, 2 * Math.PI);
        this.ctx.fill();
    }

    update(width, height) {
        if (((this.x + this.size) >= width) || ((this.x - this.size) <= 0)) {
            this.velX = -(this.velX);
        }

        if (((this.y + this.size) >= height) || ((this.y - this.size) <= 0)) {
            this.velY = -(this.velY);
        }

        this.x += this.velX;
        this.y += this.velY;
    }

    collisionDetect(balls) {
        for (const ball of balls){
            if (this !== ball) {
                const dx = (this.x - ball.x);
                const dy = (this.y - ball.y);
                const distance = Math.sqrt(dx * dx + dy * dy);

                if (distance < this.size + ball.size) {
                    this.color = randomRGB();
                }
            }
        }
    }
}

export {Ball};