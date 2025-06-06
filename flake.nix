{
  description = "Dev environment for kafka-python-example";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux"; # Adjust this if you're using a different system
      pkgs = nixpkgs.legacyPackages.${system};
    in {
      devShells.${system}.default = pkgs.mkShell {
        buildInputs = with pkgs; [
          python3Full
          uv
          kcat
          inetutils
          docker-compose
          docker
        ];
        shellHook = ''
          alias compose="docker compose"
          
          uv sync
          echo "activating virtual environment..."
          source .venv/bin/activate
          echo "Development environment for kafka-python-example is ready!"
        '';
      };
    };
}
