<script lang="ts">
  import { onMount } from "svelte";

  import Typewriter from "svelte-typewriter";
  import Footer from "../lib/Footer.svelte";
  import Button from "../shared/Button.svelte";

  let displayed = false;
  onMount(() => {
    displayed = true;
  });

  const handleNavigate = (path: string) => {
    window.location.href = path;
  };
</script>

<main>
  <div class="wrapper">
    <div class="typing">
      <Typewriter delay={1000}>Thank you for using</Typewriter>
      <Typewriter
        mode={"scramble"}
        delay={3000}
        showCursorOnDelay={true}
        keepCursorOnFinish={true}>DOCUTRACKER</Typewriter
      >
    </div>
    <div class="button-wrapper">
      <span>Get Started</span>
      <div class="buttons">
        <Button on:click={() => handleNavigate("/auth/login")}>Login</Button>
        <Button on:click={() => handleNavigate("/auth/signup")}>Signup</Button>
      </div>
    </div>
  </div>
  <Footer></Footer>
</main>

<style>
  main {
    position: fixed;
    inset: 0;
    display: flex;
    justify-content: space-evenly;
    flex-direction: column;

    & div.wrapper {
      width: 100%;
      text-align: center;

      & div.typing {
        height: 10rem;
        margin-bottom: 1rem;

        & div.typewriter-container > * {
          font-size: 2.3rem;
          font-weight: 900;
          color: var(--scroll-color);
        }
      }

      & div.button-wrapper {
        display: flex;
        justify-content: center;
        flex-direction: column;
        align-items: center;
        row-gap: 1rem;
        height: 20rem;
        background-color: var(--header-color);

        & span {
          font-size: 1.2rem;
          font-weight: 700;
        }

        & div.buttons {
          display: flex;
          justify-content: center;
          align-items: center;
          column-gap: 1rem;
        }

        & div.buttons > * {
          width: 15rem;
        }
      }
    }
  }

  /* div.typing {
    flex: 1;
    display: grid;
    place-items: center;
  }

  div.docutracker-message {
    width: 31ch;
    animation:
      typing 2000ms steps(30),
      blink 500ms step-end infinite alternate;
    white-space: nowrap;
    overflow: hidden;
    font-family: monospace;
    border-right: 2px solid;
    font-size: 2.5em;
  }

  @keyframes typing {
    from {
      width: 0;
    }
  }

  @keyframes blink {
    50% {
      border-color: transparent;
    }
  } */
</style>
