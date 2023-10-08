<script>
  import { fetchData } from "../../stores";

  import UserIcon from "../assets/userIcon.svelte";
  // @ts-ignore
  $: userName = $fetchData.user_name;
</script>

<div>
  <h1>Hello, {userName !== undefined ? userName : "Anonymous"}</h1>
  <UserIcon />
</div>

<style>
  div {
    position: sticky;
    top: 0;
    z-index: 1;

    background-color: var(--main-col-2);
    padding: 0 calc(var(--size-1) * 0.3);
    height: var(--size-3);

    display: flex;
    justify-content: space-between;
    align-items: center;

    & h1 {
      color: var(--main-col-3);
    }
  }
</style>
