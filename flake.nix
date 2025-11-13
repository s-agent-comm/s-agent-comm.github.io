{
  description = "A flake for building the Agent Semantic Communication Ontology";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      supportedSystems = [ "x86_64-linux" "aarch64-darwin" ];
      forAllSystems = f: nixpkgs.lib.genAttrs supportedSystems (system: f system);
    in
    {
      packages = forAllSystems (system: 
        let
          pkgs = nixpkgs.legacyPackages.${system};
        in
        {
          default = pkgs.stdenv.mkDerivation {
            name = "agent-semantic-communication-ontology";
            src = self;
            buildPhase = ''
              find ontologies -name "*.ttl" ! -path "ontologies/examples/*" -exec cat {} + > agent-semantic-communication.ttl
            '';
            installPhase = ''
              mkdir -p $out
              cp agent-semantic-communication.ttl $out/
            '';
          };
        }
      );
    };
}
