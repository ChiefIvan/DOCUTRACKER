<script>
  import { navExpand, dark } from "../../store";
</script>

<div class="burger-wrapper">
  <input
    class="burger-trigger"
    name="burger"
    type="checkbox"
    bind:checked={$navExpand}
  />
  <div class="burger" class:active={$navExpand} class:dark={$dark} />
</div>

<style>
  div.burger-wrapper,
  input.burger-trigger,
  div.burger {
    width: 1.3rem;
  }

  div.burger-wrapper {
    position: relative;
    display: flex;
    align-items: center;

    & input.burger-trigger {
      height: 1.5rem;
      cursor: pointer;
      opacity: 0;
    }

    & div.burger {
      transition: all ease-in-out 300ms;
      height: 0.28rem;
      background-color: var(--main-col-1);
      position: absolute;
      inset: 0;
      border-radius: 0.5rem;
      z-index: -1;
      margin: auto;
    }

    & div.burger::before,
    div.burger::after {
      transition: all ease-in-out 300ms;
      border-radius: 0.5rem;
      content: "";
      position: absolute;
      width: 1.8rem;
      height: 0.28rem;
      background-color: var(--main-col-1);
    }

    & div.burger.dark,
    div.burger.dark::before,
    div.burger.dark::after {
      background-color: var(--icon-active-color);
    }

    & div.burger::before {
      top: 7px;
    }

    & div.burger::after {
      top: -7px;
    }

    & div.burger.active {
      transform: translateX(-1rem);
      width: 0;
    }

    & div.burger.active::before,
    div.burger.active::after {
      top: 0;
    }

    & div.burger.active::before {
      transform: rotateZ(45deg);
    }

    & div.burger.active::after {
      transform: rotateZ(-45deg);
    }
  }
</style>
