import {Ball} from './Ball.js';
import { random, randomRGB } from './utils.js';

function setupCanvas() {
    // Setup canvas
    const canvas = document.querySelector("canvas");
    const ctx = canvas.getContext("2d");

    const width = (canvas.width = window.innerWidth);
    const height = (canvas.height = window.innerHeight);

    return [ctx, width, height];
}

function createBalls(ctx, width, height) {
    const balls = []

    while (balls.length < 25) {
        const size = random(10, 20);
        const ball = new Ball(
            random(0 + size, width - size),
            random(0 + size, height - size),
            random(-7, 7),
            random(-7, 7),
            randomRGB(),
            size,
            ctx,
        );

        balls.push(ball);
    }

    return balls;
}



function animation_loop(balls, width, height, ctx) {
    ctx.fillStyle = "rgba(0, 0, 0, 0.1)";
    ctx.fillRect(0, 0, width, height);

    for (const ball of balls) {
        ball.draw();
        ball.update(width, height);
        ball.collisionDetect(balls);
    }

    requestAnimationFrame(function() {
        animation_loop(balls, width, height, ctx);
    });
}

function main() {
    // Setup the canvas
    const [ctx, width, height] = setupCanvas();

    // Create balls
    const balls = createBalls(ctx, width, height);

    // Start the animation
    animation_loop(balls, width, height, ctx);
}

main();
