<script>
  export let btnName = "";
  export let btnLoginSize = false;
  export let btnSignupSize = false;
  export let btnDisabled = false;
  export let btnTitle = "";
</script>

<button
  class:change-login-size={btnLoginSize}
  class:change-signup-size={btnSignupSize}
  class:btn-disabled={btnDisabled}
  type="submit"
  title={btnName !== "Submit" ? btnTitle : btnDisabled ? btnTitle : "Submit"}
  disabled={btnDisabled}
  on:click
>
  {btnName}
</button>

<style>
  button {
    height: 2rem;
    border: none;
    color: var(--bg);
    background-color: var(--brdr-hovr);
    cursor: pointer;
    border-radius: 5px;
    transition: all ease-in-out calc(var(--dur) / 2);
  }

  button.change-login-size {
    width: 100%;
  }

  button.change-signup-size {
    width: 8rem;
  }

  button:hover {
    opacity: var(--opacity);
    box-shadow: 5px 5px 25px var(--main-col-1);
  }

  button.btn-disabled {
    background-color: var(--main-col-1);
    box-shadow: none;
    opacity: 1;
    cursor: not-allowed;
  }
</style>
