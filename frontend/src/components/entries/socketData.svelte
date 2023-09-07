<!-- <script>
  import { onMount } from "svelte";
  import io from "socket.io-client";

  let socket;

  onMount(() => {
    socket = io("http://localhost:5000");

    socket.on("login_status", function (data) {
      console.log(data["is_logged_in"]);
    });
  });
</script> -->
