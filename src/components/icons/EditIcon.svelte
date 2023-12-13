<script>
  import { dark } from "../../store";
</script>

<svg class:dark={$dark} xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
  ><path
    class:dark={$dark}
    fill="currentColor"
    d="M3 17.46v3.04c0 .28.22.5.5.5h3.04c.13 0 .26-.05.35-.15L17.81 9.94l-3.75-3.75L3.15 17.1c-.1.1-.15.22-.15.36zM20.71 5.63l-2.34-2.34a.996.996 0 0 0-1.41 0l-1.83 1.83l3.75 3.75l1.83-1.83a.996.996 0 0 0 0-1.41z"
  /></svg
>

<style>
  svg {
    width: 1.8rem;
    height: 1.8rem;
    transition: all ease-in-out 300ms;
    border-radius: 50%;
    cursor: pointer;
    padding: 0.3rem;

    & path {
      fill: var(--main-col-1);
      transition: all ease-in-out 300ms;
    }
  }

  svg:hover {
    background-color: var(--main-col-1);
  }

  svg.dark:hover {
    background-color: var(--dark-main-col-2);
  }

  svg:hover path {
    fill: var(--background);
  }
</style>
