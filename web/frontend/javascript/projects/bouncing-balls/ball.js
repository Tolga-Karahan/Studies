import { random, randomRGB } from './utils.js';

class Shape {
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
            if (this !== ball && this.exists) {
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
class Ball extends Shape {
    constructor(x, y, velX, velY, color, size, ctx) {
        super(x, y, velX, velY, color, size, ctx);
        this.exists = true;
    }
}

class EvilBall extends Shape{
    constructor(x, y, ctx) {
        super(x, y, 20, 20, "rgb(255, 255, 255)", 30, ctx);
        this.killed = 0;
        window.addEventListener("keydown", (e) => {
            switch (e.key) {
                case "a":
                    this.x -= this.velX;
                    break;
                case "s":
                    this.y += this.velY;
                    break;
                case "d":
                    this.x += this.velX;
                    break;
                case "w":
                    this.y -= this.velY;
                    break;
            }
        });
    }

    draw() {
        this.ctx.beginPath();
        this.ctx.strokeStyle = this.color;
        this.ctx.lineWidth = 3;
        this.ctx.arc(this.x, this.y, this.size, 0, 2 * Math.PI);
        this.ctx.stroke();
    }

    collisionDetect(balls) {
        for (const ball of balls){
            if (ball.exists) {
                const dx = (this.x - ball.x);
                const dy = (this.y - ball.y);
                const distance = Math.sqrt(dx * dx + dy * dy);

                if (distance < this.size + ball.size) {
                    this.killed++;
                    ball.exists = false;
                }
            }
        }
    }
}

export {Ball, EvilBall};