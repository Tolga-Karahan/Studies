import {Ball, EvilBall} from './Ball.js';
import { random, randomRGB } from './utils.js';

const BALL_COUNT = 25;

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

    while (balls.length < BALL_COUNT) {
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



function animation_loop(evil_ball, balls, width, height, ctx) {
    ctx.fillStyle = "rgba(0, 0, 0, 0.1)";
    ctx.fillRect(0, 0, width, height);

    evil_ball.draw();
    evil_ball.collisionDetect(balls);

    const score_p = document.querySelector("p");
    score_p.textContent = `Ball count: ${BALL_COUNT - evil_ball.killed}`;

    for (const ball of balls) {
        if (ball.exists) {
            ball.draw();
            ball.update(width, height);
            ball.collisionDetect(balls);
        }
    }

    if (evil_ball.killed === BALL_COUNT) {
        alert("Congrats! You killed all the balls!")
    }

    requestAnimationFrame(function() {
        animation_loop(evil_ball, balls, width, height, ctx);
    });
}

function main() {
    // Setup the canvas
    const [ctx, width, height] = setupCanvas();

    // Create the evil ball
    const evil_ball = new EvilBall(
        random(0 + 10, width - 10),
        random(0 + 10, height - 10),
        ctx
    )

    // Create balls
    const balls = createBalls(ctx, width, height);

    // Start the animation
    animation_loop(evil_ball, balls, width, height, ctx);
}

main();
